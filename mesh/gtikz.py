#!/usr/bin/python3

import argparse
from pprint import pprint


def gen_tikz(file_name, points, edges, dots):
    with open(file_name, 'w') as file:
        file.write("\\begin{tikzpicture}\n")
        for dot in dots:
            file.write("\\filldraw [gray] ({},{}) circle (2pt);\n".format(
                dot[0], dot[1]))
        for edg in edges:
            file.write("\\draw ({},{}) -- ({},{});\n".format(
                points[edg[0]][0], points[edg[0]][1], points[edg[1]][0],
                points[edg[1]][1]))
        file.write("\\end{tikzpicture}\n")


def gen_svg(file_name, width, height, points, edges, dots):
    if dots:
        xmax = max([max([x[0] for x in points]), max([x[0] for x in dots])])
        xmin = min([min([x[0] for x in points]), min([x[0] for x in dots])])
        ymax = max([max([x[1] for x in points]), max([x[1] for x in dots])])
        ymin = min([min([x[1] for x in points]), min([x[1] for x in dots])])
    else:
        xmax = max([x[0] for x in points])
        xmin = min([x[0] for x in points])
        ymax = max([x[1] for x in points])
        ymin = min([x[1] for x in points])
    dmax = max(xmax - xmin, ymax - ymin)
    points = [((x[0] - xmin) / dmax, (x[1] - ymin) / dmax) for x in points]
    dots = [((x[0] - xmin) / dmax, (x[1] - ymin) / dmax) for x in dots]
    with open(file_name, 'w') as file:
        file.write('<svg width="{}" height="{}">\n'.format(width, height))
        file.write(
            '<rect x="0" y="0" width="{}" height="{}" fill="white" stroke="white"/>'.
            format(width, height))
        for dot in dots:
            file.write(
                '<circle cx="{}" cy="{}" r="2" fill="gray" stroke="gray" />\n'.
                format(
                    int(0.9 * width * dot[0]) + int(width * 0.05),
                    height - int(0.9 * height * dot[1]) - int(height * 0.05)))
        for edg in edges:
            file.write(
                '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke-width="2" stroke="black" />\n'.
                format(
                    int(0.9 * width * points[edg[0]][0]) + int(width * 0.05),
                    height - int(0.9 * height * points[edg[0]][1]) -
                    int(height * 0.05),
                    int(0.9 * width * points[edg[1]][0]) + int(width * 0.05),
                    height - int(0.9 * height * points[edg[1]][1]) - int(
                        height * 0.05)))
        file.write("</svg>\n")


def poly(args):
    with open(args.file) as file:
        lines = [x.split() for x in file.readlines()]
    points = []
    edges = []
    holes = []
    pcount = int(lines[0][0])
    lines.pop(0)
    for i in range(pcount):
        points.append((float(lines[i][1]), float(lines[i][2])))
    lines = lines[pcount:]
    ecount = int(lines[0][0])
    lines.pop(0)
    for i in range(ecount):
        edges.append((int(lines[i][1]) - 1, int(lines[i][2]) - 1))
    lines = lines[ecount:]
    hcount = int(lines[0][0])
    lines.pop(0)
    for i in range(hcount):
        holes.append((float(lines[i][1]), float(lines[i][2])))
    lines = lines[hcount:]
    gen_tikz("{}.tex".format(args.o), points, edges, holes)
    if args.svg:
        gen_svg("{}.svg".format(args.o), args.width, args.height, points, edges,
                holes)


def node(args):
    with open("{}.node".format(args.file)) as file:
        node_lines = [x.split() for x in file.readlines()]
    with open("{}.ele".format(args.file)) as file:
        ele_lines = [x.split() for x in file.readlines()]
    pcount = int(node_lines[0][0])
    points = []
    triangles = []
    node_lines.pop(0)
    for i in range(pcount):
        points.append((float(node_lines[i][1]), float(node_lines[i][2])))
    tcount = int(ele_lines[0][0])
    ele_lines.pop(0)
    for i in range(tcount):
        triangles.append((int(ele_lines[i][1]) - 1, int(ele_lines[i][2]) - 1,
                          int(ele_lines[i][3]) - 1))
    edges = []
    for tri in triangles:
        e1 = (tri[0], tri[1])
        e2 = (tri[1], tri[2])
        e3 = (tri[2], tri[0])
        if e1 not in edges:
            edges.append(e1)
        if e2 not in edges:
            edges.append(e2)
        if e3 not in edges:
            edges.append(e3)
    gen_tikz("{}.tex".format(args.o), points, edges, [])
    if args.svg:
        gen_svg("{}.svg".format(args.o), args.width, args.height, points, edges,
                [])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="File name to generate tikz/svg for")
    parser.add_argument(
        '--svg', action='store_true', help="Generates svg image")
    parser.add_argument('-o', nargs='?', help="Output file name")
    parser.add_argument(
        '--width', default=1000, type=int, help='Sets image width for svg')
    parser.add_argument(
        '--height', default=1000, type=int, help='Sets image height for svg')
    args = parser.parse_args()
    if args.o == None:
        args.o = args.file
    if args.file.endswith('.poly'):
        poly(args)
    else:
        node(args)


if __name__ == "__main__":
    main()
