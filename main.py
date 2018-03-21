import fileinput
import os
import sys


def assign_list(main_list, place, list_name, num):
    for i in range(place, place + num):
        sub_list = []
        sub_list.append(int(main_list[i][0]))
        sub_list.append(int(main_list[i][1]))
        list_name.append(sub_list)


def main():
    folder = sys.argv[1]
    if os.path.exists(folder):
        print(folder)

    alpha_filename = folder + "/" + "alpha.in"
    arch_filename = folder + "/" + "arch.in"
    graphs_filename = folder + "/" + "graphs.in"
    ops_filename = folder + "/" + "ops.in"

    # Alpha file
    alpha_file = open(alpha_filename)
    print("Alpha")
    alpha = 0
    for line in alpha_file:
        alpha = float(line)
    print("\talpha", alpha)

    # Arch file
    arch_file = open(arch_filename)
    print("Arch")
    arch_list = []
    for line in arch_file:
        arch_sub_list = []
        for val in line.split():
            arch_sub_list.append(val)
        arch_list.append(arch_sub_list)

    rows = int(arch_list[0][0])
    columns = int(arch_list[0][1])
    num_input_res = int(arch_list[1][0])
    num_output_res = int(arch_list[1][1])
    num_sensors = int(arch_list[2][0])
    num_detectors = int(arch_list[2][1])
    num_heaters = int(arch_list[2][2])

    curr_place_in_list = 3

    loc_input_res_list = []
    assign_list(arch_list, curr_place_in_list, loc_input_res_list,
                num_input_res)
    curr_place_in_list = curr_place_in_list + num_input_res

    loc_output_res_list = []
    assign_list(arch_list, curr_place_in_list, loc_output_res_list,
                num_output_res)
    curr_place_in_list = curr_place_in_list + num_output_res

    loc_sensors_list = []
    assign_list(arch_list, curr_place_in_list, loc_sensors_list, num_sensors)
    curr_place_in_list = curr_place_in_list + num_sensors

    loc_detectors_list = []
    assign_list(arch_list, curr_place_in_list, loc_detectors_list,
                num_detectors)
    curr_place_in_list = curr_place_in_list + num_detectors

    loc_heaters_list = []
    assign_list(arch_list, curr_place_in_list, loc_heaters_list, num_heaters)
    curr_place_in_list = curr_place_in_list + num_heaters

    print("\trows", rows)
    print("\tcols", columns)
    print("\tnum input res", num_input_res)
    print("\tnum output res", num_output_res)
    print("\tnum sensors", num_sensors)
    print("\tnum detectors", num_detectors)
    print("\tnum heaters", num_heaters)
    print("\tloc input res", loc_input_res_list)
    print("\tloc output res", loc_output_res_list)
    print("\tloc sensors", loc_sensors_list)
    print("\tloc detectors", loc_detectors_list)
    print("\tloc heaters", loc_heaters_list)

    # Graphs file
    graphs_file = open(graphs_filename)
    print("Graphs")
    graphs_list = []
    for line in graphs_file:
        graphs_sub_list = []
        for val in line.split():
            graphs_sub_list.append(val)
        graphs_list.append(graphs_sub_list)

    num_vertices_graphs = int(graphs_list[0][0])
    num_edges_interference = int(graphs_list[0][1])
    num_edges_communication = int(graphs_list[0][2])

    curr_place_in_list = 1

    edge_set_interference_list = []
    assign_list(graphs_list, curr_place_in_list, edge_set_interference_list,
                num_edges_interference)
    curr_place_in_list = curr_place_in_list + num_edges_interference

    edge_set_communication_list = []
    for i in range(curr_place_in_list,
                   curr_place_in_list + num_edges_communication):
        sub_list = []
        sub_list.append(int(graphs_list[i][0]))
        sub_list.append(int(graphs_list[i][1]))
        sub_list.append(int(graphs_list[i][2]))
        edge_set_communication_list.append(sub_list)
    curr_place_in_list = curr_place_in_list + num_edges_communication

    print("\tnum vert", num_vertices_graphs)
    print("\tnum edges inter", num_edges_interference)
    print("\tnum edges commun", num_edges_communication)
    print("\tedge set inter", edge_set_interference_list)
    print("\tedge set commun", edge_set_communication_list)

    # Ops file
    ops_file = open(ops_filename)
    print("Ops")
    ops_list = []
    for line in ops_file:
        ops_sub_list = []
        for val in line.split():
            ops_sub_list.append(val)
        ops_list.append(ops_sub_list)

    num_ops_assay = int(ops_list[0][0])

    input_ops_list = []  # [[assay id, r_id]]
    output_ops_list = []  # [[assay id, r_id]]
    mixing_ops_list = []  # [[assay id, cost]]
    split_ops_list = []  # [assay id]
    merge_ops_list = []  # [assay id]
    store_ops_list = []  # [assay id]
    sense_ops_list = []  # [assay id]
    detect_ops_list = []  # [assay id]
    heat_ops_list = []  # [assay id]

    for i in range(1, 1 + num_ops_assay):
        sub_list = []
        sub_list.append(i)
        if int(ops_list[i][0]) == 1:
            sub_list.append(int(ops_list[i][1]))
            input_ops_list.append(sub_list)
        elif int(ops_list[i][0]) == 2:
            sub_list.append(int(ops_list[i][1]))
            output_ops_list.append(sub_list)
        elif int(ops_list[i][0]) == 3:
            sub_list.append(float(ops_list[i][1]))
            mixing_ops_list.append(sub_list)
        elif int(ops_list[i][0]) == 4:
            split_ops_list.append(sub_list)
        elif int(ops_list[i][0]) == 5:
            merge_ops_list.append(sub_list)
        elif int(ops_list[i][0]) == 6:
            store_ops_list.append(sub_list)
        elif int(ops_list[i][0]) == 7:
            sense_ops_list.append(sub_list)
        elif int(ops_list[i][0]) == 8:
            detect_ops_list.append(sub_list)
        elif int(ops_list[i][0]) == 9:
            heat_ops_list.append(sub_list)

    print("\tnum ops", num_ops_assay)
    print("\tinput", input_ops_list)
    print("\toutput", output_ops_list)
    print("\tmixing", mixing_ops_list)
    print("\tsplit", split_ops_list)
    print("\tmerge", merge_ops_list)
    print("\tstore", store_ops_list)
    print("\tsense", sense_ops_list)
    print("\tdetect", detect_ops_list)
    print("\theat", heat_ops_list)


if __name__ == "__main__":
    main()
