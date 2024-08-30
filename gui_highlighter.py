from PIL import Image, ImageDraw
import os
import re

def parse_bounds(node):
    top_left = node["bounds"][0].split(',')
    bottom_right = node["bounds"][1].split(',')
    for i in range(2):
        top_left[i] = int(top_left[i])
        bottom_right[i] = int(bottom_right[i])
    return (tuple(top_left), tuple(bottom_right))

def draw_box(draw, node):
    top_left, bottom_right = parse_bounds(node)
    if node["clickable"]:
        color = "yellow"
        width = 8
    else:
        color = "red"
        width = 3
    draw.rectangle([top_left, bottom_right], outline=color, width=width)

def get_node_attr(file) -> list:
    nodes = {}
    with open(file, 'r') as f:
        output = f.read()      
            
    for i in range(len(output)):
        if i < len(output) - 5 and output[i:i+5] == "<node":
            i += 5
            nodes[len(nodes)] = {}
        if output[i] == " " and i < len(output) - 10:
            if output[i+1:i+8] == "bounds=":
                i += 10
                top_left, bottom_right = "", ""
                while output[i] != "]":
                    top_left += output[i]
                    i += 1
                i += 2
                while output[i] != "]":
                    bottom_right += output[i]
                    i += 1
                nodes[len(nodes)-1]["bounds"] = (top_left, bottom_right)
            elif output[i+1:i+11] == "clickable=":
                i += 12
                is_clickable = (output[i] == "t")
                nodes[len(nodes)-1]["clickable"] = is_clickable         
            
    return nodes
    
data = sorted(os.listdir('data')) # Sort directory to guarantee correct file couplings
if not os.path.exists("output"):
    os.mkdir("output")
# Iterate through every xml file
for i in range(1, len(data), 2):
    image = data[i-1]
    meta_data = data[i]
    nodes = get_node_attr('data/' + meta_data)
    with Image.open('data/' + image) as img:
        draw = ImageDraw.Draw(img, 'RGBA')
        for i in range(len(nodes)):
            draw_box(draw, nodes[i])

    img.save(os.path.join("output", f"{image}-HIGHLIGHTED.png"))
