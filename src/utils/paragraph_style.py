def Set_paragraph_style(paragraph, alignment, space_after, space_before, text_size):
    """
    Set the style of a paragraph.
    
    :param paragraph: The paragraph to style.
    :param alignment: Text alignment ('left', 'center', 'right', 'justify').
    :param space_after: Space after the paragraph in points.
    :param space_before: Space before the paragraph in points.
    """
    if alignment == 'left':
        paragraph.alignment = 0  # WD_ALIGN_PARAGRAPH.LEFT
    elif alignment == 'center':
        paragraph.alignment = 1  # WD_ALIGN_PARAGRAPH.CENTER
    elif alignment == 'right':
        paragraph.alignment = 2  # WD_ALIGN_PARAGRAPH.RIGHT
    elif alignment == 'justify':
        paragraph.alignment = 3  # WD_ALIGN_PARAGRAPH.JUSTIFY
    
    paragraph.space_after = space_after
    paragraph.space_before = space_before
    paragraph.text_size = text_size 
    paragraph.paragraph_format.space_before = 18