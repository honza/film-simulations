import json
import os


def validate(config, simulation):
    name = simulation.get('name')
    if not name:
        print('ERROR: missing name')
        return False

    print(name)

    options = config['options']
    order = config['order']

    option_keys = set(options.keys())
    simulation_keys = set(simulation.keys())

    missing_keys = option_keys.difference(simulation_keys)

    if missing_keys:
        print('  ERROR: missing keys:', ', '.join(missing_keys))
        return False

    for key in order:
        allowed = options[key]
        value = simulation[key]

        if allowed is None:
            continue

        if value in allowed:
            continue

        print('  fail  ', key)
        return False

    return True



def main():
    config = json.loads(open('config.json').read())
    simulations = []

    for f in os.listdir('simulations'):
        simulations.append(
            json.loads(
                open(
                    os.path.join('simulations', f)
                ).read()
            )
        )

    for simulation in simulations:
        validate(config, simulation)


if __name__ == '__main__':
    main()
