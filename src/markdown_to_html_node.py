from parentnode import ParentNode
from leafnode import LeafNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html
from markdown_to_blocks import markdown_to_blocks
from BlockType import block_to_block_type, BlockType


def markdown_to_html_node(markdown):
    """
    Convert a full markdown document into a single ParentNode (div) containing
    child HTML nodes for each block in the document.
    """
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        btype = block_to_block_type(block)

        if btype == BlockType.HEADING:
            # count leading #'s
            i = 0
            while i < len(block) and block[i] == '#':
                i += 1
            level = max(1, min(6, i))
            # heading text after '# ' (assume proper format)
            text = block[i+1:]
            inline_nodes = text_to_textnodes(text)
            children.append(ParentNode(f"h{level}", [text_node_to_html(n) for n in inline_nodes]))

        elif btype == BlockType.CODE:
            # remove the starting and ending ``` and keep raw content
            if block.startswith("```") and block.endswith("```"):
                inner = block[3:-3]
                # strip a leading newline if present
                if inner.startswith('\n'):
                    inner = inner[1:]
                # strip trailing newline
                if inner.endswith('\n'):
                    inner = inner[:-1]
            else:
                inner = block
            # put code inside pre > code
            code_leaf = LeafNode("code", inner)
            pre_node = ParentNode("pre", [code_leaf])
            children.append(pre_node)

        elif btype == BlockType.QUOTE:
            # strip leading "> " from each line, or just ">" for blank quote lines
            lines = []
            for line in block.split('\n'):
                if line.startswith("> "):
                    lines.append(line[2:])
                elif line == ">":
                    lines.append("")
                else:
                    lines.append(line)
            quote_text = "\n".join(lines)
            inline_nodes = text_to_textnodes(quote_text)
            children.append(ParentNode("blockquote", [text_node_to_html(n) for n in inline_nodes]))

        elif btype == BlockType.UNORDERED_LIST:
            items = []
            for line in block.split('\n'):
                # remove leading "- "
                item_text = line[2:] if line.startswith("- ") else line
                inline_nodes = text_to_textnodes(item_text)
                li = ParentNode("li", [text_node_to_html(n) for n in inline_nodes])
                items.append(li)
            children.append(ParentNode("ul", items))

        elif btype == BlockType.ORDERED_LIST:
            items = []
            for line in block.split('\n'):
                # remove leading numbering like "1. "
                parts = line.split('. ', 1)
                item_text = parts[1] if len(parts) > 1 else line
                inline_nodes = text_to_textnodes(item_text)
                li = ParentNode("li", [text_node_to_html(n) for n in inline_nodes])
                items.append(li)
            children.append(ParentNode("ol", items))

        else:
            # paragraph
            inline_nodes = text_to_textnodes(block)
            children.append(ParentNode("p", [text_node_to_html(n) for n in inline_nodes]))

    # wrap all block nodes in a div
    return ParentNode("div", children)
