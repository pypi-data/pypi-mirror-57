import csv
import json
import sys

import click
import yaml

import osxphotos

from ._version import __version__

# TODO: add "--any" to search any field (e.g. keyword, description, name contains "wedding") (add case insensitive option)


class CLI_Obj:
    def __init__(self, db=None, json=False, debug=False):
        if debug:
            osxphotos._debug(True)
        self.photosdb = osxphotos.PhotosDB(dbfile=db)
        self.json = json


CTX_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CTX_SETTINGS)
@click.option(
    "--db",
    required=False,
    metavar="<Photos database path>",
    default=None,
    help="Specify database file",
)
@click.option(
    "--json",
    required=False,
    is_flag=True,
    default=False,
    help="Print output in JSON format",
)
@click.option("--debug", required=False, is_flag=True, default=False, hidden=True)
@click.version_option(__version__, "--version", "-v")
@click.pass_context
def cli(ctx, db, json, debug):
    ctx.obj = CLI_Obj(db=db, json=json, debug=debug)


@cli.command()
@click.pass_obj
def keywords(cli_obj):
    """ print out keywords found in the Photos library"""
    keywords = {"keywords": cli_obj.photosdb.keywords_as_dict()}
    if cli_obj.json:
        print(json.dumps(keywords))
    else:
        print(yaml.dump(keywords, sort_keys=False))


@cli.command()
@click.pass_obj
def albums(cli_obj):
    """ print out albums found in the Photos library """
    albums = {"albums": cli_obj.photosdb.albums_as_dict()}
    if cli_obj.json:
        print(json.dumps(albums))
    else:
        print(yaml.dump(albums, sort_keys=False))


@cli.command()
@click.pass_obj
def persons(cli_obj):
    """ print out persons (faces) found in the Photos library """
    persons = {"persons": cli_obj.photosdb.persons_as_dict()}
    if cli_obj.json:
        print(json.dumps(persons))
    else:
        print(yaml.dump(persons, sort_keys=False))


@cli.command()
@click.pass_obj
def info(cli_obj):
    """ print out descriptive info of the Photos library database """
    pdb = cli_obj.photosdb
    info = {}
    info["database_path"] = pdb.get_db_path()
    info["database_version"] = pdb.get_db_version()

    photos = pdb.photos()
    info["photo_count"] = len(photos)

    keywords = pdb.keywords_as_dict()
    info["keywords_count"] = len(keywords)
    info["keywords"] = keywords

    albums = pdb.albums_as_dict()
    info["albums_count"] = len(albums)
    info["albums"] = albums

    persons = pdb.persons_as_dict()
    # handle empty person names (added by Photos 5.0+ when face detected but not identified)
    noperson = "UNKNOWN"
    if "" in persons:
        if noperson in persons:
            persons[noperson].append(persons[""])
        else:
            persons[noperson] = persons[""]
        persons.pop("", None)

    info["persons_count"] = len(persons)
    info["persons"] = persons

    if cli_obj.json:
        print(json.dumps(info))
    else:
        print(yaml.dump(info, sort_keys=False))


@cli.command()
@click.pass_obj
def dump(cli_obj):
    """ print list of all photos & associated info from the Photos library """
    pdb = cli_obj.photosdb
    photos = pdb.photos()
    print_photo_info(photos, cli_obj.json)


@cli.command()
@click.option("--keyword", default=None, multiple=True, help="search for keyword(s)")
@click.option("--person", default=None, multiple=True, help="search for person(s)")
@click.option("--album", default=None, multiple=True, help="search for album(s)")
@click.option("--uuid", default=None, multiple=True, help="search for UUID(s)")
@click.option(
    "--name", default=None, multiple=True, help="search for TEXT in name of photo"
)
@click.option("--no-name", is_flag=True, help="search for photos with no name")
@click.option(
    "--description",
    default=None,
    multiple=True,
    help="search for TEXT in description of photo",
)
@click.option(
    "--no-description", is_flag=True, help="search for photos with no description"
)
@click.option(
    "-i",
    "--ignore-case",
    is_flag=True,
    help="case insensitive search for name or description. Does not apply to keyword, person, or album",
)
@click.option("--favorite", is_flag=True, help="search for photos marked favorite")
@click.option(
    "--not-favorite", is_flag=True, help="search for photos not marked favorite"
)
@click.option("--hidden", is_flag=True, help="search for photos marked hidden")
@click.option("--not-hidden", is_flag=True, help="search for photos not marked hidden")
@click.option("--missing", is_flag=True, help="search for photos missing from disk")
@click.option(
    "--not-missing",
    is_flag=True,
    help="search for photos present on disk (e.g. not missing)",
)
@click.option(
    "--json",
    required=False,
    is_flag=True,
    default=False,
    help="Print output in JSON format",
)
@click.pass_obj
@click.pass_context
def query(
    ctx,
    cli_obj,
    keyword,
    person,
    album,
    uuid,
    name,
    no_name,
    description,
    no_description,
    ignore_case,
    json,
    favorite,
    not_favorite,
    hidden,
    not_hidden,
    missing,
    not_missing,
):
    """ query the Photos database using 1 or more search options; 
        if more than one option is provided, they are treated as "AND" 
        (e.g. search for photos matching all options)
    """

    # if no query terms, show help and return
    if not any(
        [
            keyword,
            person,
            album,
            uuid,
            name,
            no_name,
            description,
            no_description,
            favorite,
            not_favorite,
            hidden,
            not_hidden,
            missing,
            not_missing,
        ]
    ):
        print(cli.commands["query"].get_help(ctx))
        return
    elif favorite and not_favorite:
        # can't search for both favorite and notfavorite
        print(cli.commands["query"].get_help(ctx))
        return
    elif hidden and not_hidden:
        # can't search for both hidden and nothidden
        print(cli.commands["query"].get_help(ctx))
        return
    elif missing and not_missing:
        # can't search for both missing and notmissing
        print(cli.commands["query"].get_help(ctx))
        return
    elif name and no_name:
        # can't search for both name and no_name
        print(cli.commands["query"].get_help(ctx))
        return
    elif description and no_description:
        # can't search for both description and no_description
        print(cli.commands["query"].get_help(ctx))
        return
    else:
        photos = cli_obj.photosdb.photos(
            keywords=keyword, persons=person, albums=album, uuid=uuid
        )

        if name:
            # search name field for text
            # if more than one, find photos with all name values in in name
            if ignore_case:
                # case-insensitive
                for n in name:
                    n = n.lower()
                    photos = [p for p in photos if p.name() and n in p.name().lower()]
            else:
                for n in name:
                    photos = [p for p in photos if p.name() and n in p.name()]
        elif no_name:
            photos = [p for p in photos if not p.name()]

        if description:
            # search description field for text
            # if more than one, find photos with all name values in in description
            if ignore_case:
                # case-insensitive
                for d in description:
                    d = d.lower()
                    photos = [
                        p
                        for p in photos
                        if p.description() and d in p.description().lower()
                    ]
            else:
                for d in description:
                    photos = [
                        p for p in photos if p.description() and d in p.description()
                    ]
        elif no_description:
            photos = [p for p in photos if not p.description()]

        if favorite:
            photos = [p for p in photos if p.favorite()]
        elif not_favorite:
            photos = [p for p in photos if not p.favorite()]

        if hidden:
            photos = [p for p in photos if p.hidden()]
        elif not_hidden:
            photos = [p for p in photos if not p.hidden()]

        if missing:
            photos = [p for p in photos if p.ismissing()]
        elif not_missing:
            photos = [p for p in photos if not p.ismissing()]

        print_photo_info(photos, cli_obj.json or json)


@cli.command()
@click.argument("topic", default=None, required=False, nargs=1)
@click.pass_context
def help(ctx, topic, **kw):
    """ print help; for help on commands: help <command> """
    if topic is None:
        print(ctx.parent.get_help())
    else:
        print(cli.commands[topic].get_help(ctx))


def print_photo_info(photos, json=False):
    if json:
        dump = []
        for p in photos:
            dump.append(p.to_json())
        print(f"[{', '.join(dump)}]")
    else:
        # dump as CSV
        csv_writer = csv.writer(
            sys.stdout, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        dump = []
        # add headers
        dump.append(
            [
                "uuid",
                "filename",
                "original_filename",
                "date",
                "description",
                "name",
                "keywords",
                "albums",
                "persons",
                "path",
                "ismissing",
                "hasadjustments",
                "favorite",
                "hidden",
                "latitude",
                "longitude",
                "path_edited",
            ]
        )
        for p in photos:
            dump.append(
                [
                    p.uuid(),
                    p.filename(),
                    p.original_filename(),
                    str(p.date()),
                    p.description(),
                    p.name(),
                    ", ".join(p.keywords()),
                    ", ".join(p.albums()),
                    ", ".join(p.persons()),
                    p.path(),
                    p.ismissing(),
                    p.hasadjustments(),
                    p.favorite(),
                    p.hidden(),
                    p._latitude(),
                    p._longitude(),
                    p.path_edited(),
                ]
            )
        for row in dump:
            csv_writer.writerow(row)


if __name__ == "__main__":
    cli()
