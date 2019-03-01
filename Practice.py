def multiple_text_tab_element_to_text_multiple_tabbed_element(filename):

    import io

    output_filename = 'output_' + filename
    with io.open(output_filename, 'w', encoding='utf-8') as output_file:
        with io.open(filename, 'r', encoding='utf-8') as file:
            text = "text"
            for line in file:
                original_line = []
                line_as_list = original_line + ((line.rstrip("\n")).rstrip("\t")).split("\t")
                if line_as_list[0] != text:
                    text = line_as_list[0]
                    output_file.write("\n")
                    output_file.write(line_as_list[0])
                output_file.write("\t")
                output_file.write(line_as_list[1])
