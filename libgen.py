def libgen():
    """
    Search for a book in libgen.io
    """
    title = "titulo"

    from libgen_api import LibgenSearch

    s = LibgenSearch()
    results = s.search_title(title)
    item_to_download = results[0]
    download_links = s.resolve_download_links(item_to_download)

    with open('filename.txt', 'w', encoding='utf-8') as f:
        print(results[0], download_links, file=f)

libgen()