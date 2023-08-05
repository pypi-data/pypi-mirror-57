"""Jedi Language Server

Creates the language server constant and wraps "features" with it.

Official language server spec:
    https://microsoft.github.io/language-server-protocol/specification
"""

from typing import Dict  # pylint: disable=unused-import
from typing import List, Optional

from pygls.features import (
    COMPLETION,
    DEFINITION,
    DOCUMENT_SYMBOL,
    HOVER,
    REFERENCES,
    RENAME,
)
from pygls.server import LanguageServer
from pygls.types import (
    CompletionItem,
    CompletionList,
    CompletionParams,
    DocumentSymbolParams,
    Hover,
    Location,
    RenameParams,
    SymbolInformation,
    TextDocumentPositionParams,
    TextEdit,
    WorkspaceEdit,
)

from .server_utils import (
    get_jedi_names,
    get_jedi_parent_name,
    get_jedi_script,
    get_location_from_definition,
)
from .type_map import get_lsp_type

SERVER = LanguageServer()


@SERVER.feature(COMPLETION, triggerCharacters=["."])
def lsp_completion(server: LanguageServer, params: CompletionParams = None):
    """Returns completion items."""
    script = get_jedi_script(server, params)
    jedi_completions = script.completions()
    return CompletionList(
        is_incomplete=False,
        items=[
            CompletionItem(
                label=completion.name,
                kind=get_lsp_type(completion.type),
                detail=completion.description,
                documentation=completion.docstring(),
                insert_text=completion.name,
            )
            for completion in jedi_completions
        ],
    )


@SERVER.feature(DEFINITION)
def lsp_definition(
    server: LanguageServer, params: TextDocumentPositionParams
) -> List[Location]:
    """Support Goto Definition"""
    script = get_jedi_script(server, params)
    definitions = script.goto_assignments(
        follow_imports=True, follow_builtin_imports=True
    )
    return [
        get_location_from_definition(definition) for definition in definitions
    ]


@SERVER.feature(HOVER)
def lsp_hover(
    server: LanguageServer, params: TextDocumentPositionParams
) -> Hover:
    """Support the hover feature"""
    script = get_jedi_script(server, params)
    definitions = script.goto_definitions()
    return Hover(
        contents=(
            definitions[0].docstring()
            if definitions
            else "No docstring definition found."
        )
    )


@SERVER.feature(REFERENCES)
def lsp_references(
    server: LanguageServer, params: TextDocumentPositionParams
) -> List[Location]:
    """Obtain all references to document"""
    script = get_jedi_script(server, params)
    try:
        definitions = script.usages()
    except Exception:  # pylint: disable=broad-except
        return []
    return [
        get_location_from_definition(definition) for definition in definitions
    ]


@SERVER.feature(RENAME)
def lsp_rename(
    server: LanguageServer, params: RenameParams
) -> Optional[WorkspaceEdit]:
    """Optional workspace edit"""
    script = get_jedi_script(server, params)
    definitions = script.usages()
    locations = [
        get_location_from_definition(definition) for definition in definitions
    ]
    if not locations:
        return None
    changes = {}  # type: Dict[str, List[TextEdit]]
    for location in locations:
        text_edit = TextEdit(location.range, new_text=params.newName)
        if location.uri not in changes:
            changes[location.uri] = [text_edit]
        else:
            changes[location.uri].append(text_edit)
    return WorkspaceEdit(changes=changes)


@SERVER.feature(DOCUMENT_SYMBOL)
def lsp_document_symbol(
    server: LanguageServer, params: DocumentSymbolParams
) -> List[SymbolInformation]:
    """Document Python document symbols"""
    jedi_names = get_jedi_names(server, params)
    return [
        SymbolInformation(
            name=definition.name,
            kind=get_lsp_type(definition.type),
            location=get_location_from_definition(definition),
            container_name=get_jedi_parent_name(definition),
        )
        for definition in jedi_names
    ]
