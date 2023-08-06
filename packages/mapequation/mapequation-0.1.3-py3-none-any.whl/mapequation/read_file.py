from collections import namedtuple

StateNode = namedtuple("StateNode", "state_id, physical_id")
Link = namedtuple("Link", "source, target, weight")
Tree = namedtuple("Tree", "path, flow, state_id, physical_id")


def read_net(filename, include_states=True, weight_type=float):
    states = []
    links = []

    with open(filename, "r") as f:
        context = None

        for line in f:
            if line.startswith("#"):
                continue

            l = line.lower()

            if include_states and l.startswith("*states"):
                context = "*states"
                continue
            elif l.startswith("*links"):
                context = "*links"
                continue

            if context == "*states":
                state_id, physical_id, *_ = line.split()
                states.append(StateNode(int(state_id), int(physical_id)))
            elif context == "*links":
                source, target, weight = line.split()
                links.append(Link(int(source), int(target), weight_type(weight)))

    return states, links


def read_tree(filename):
    tree = []

    with open(filename, "r") as f:
        for line in f:
            if line.startswith("#"):
                continue

            path, flow, *_, state_id, physical_id = line.split()
            path = tuple(map(int, path.split(":")))
            tree.append(Tree(path, float(flow), int(state_id), int(physical_id)))

    return tree


if __name__ == "__main__":
    net = read_net("test/training_seed0_order2_0.net")
    print(net[0])
    print(net[1])
    tree = read_tree("test/training_seed0_order2_0_states.tree")
    print(tree)
