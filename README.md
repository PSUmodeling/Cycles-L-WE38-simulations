# Cycles-L-WE38-simulation

Simulations using MM-PIHM version 1.0.0 (Cycles version 1.0.0).

## Scenarios
| Scenarios             | Fertilization multiplier  | Manure fertilizer | Synthetic fertilizer  | Switchgrass   |
|---------------------- | ------------------------- | ----------------- | --------------------- | ------------- |
| WE38                  | 1.0                       | X                 | X                     |               |
| WE38_1dot25xN         | 1.25                      | X                 | X                     |               |
| WE38_1dot5xN          | 1.5                       | X                 | X                     |               |
| WE38_lowland          | 1.25                      | X                 | X                     | H             |
| WE38_lowland_manure   | 1.25                      | X                 |                       | H             |
| WE38_upland           | 1.25                      | X                 | X                     | L             |
| WE38_upland_manure    | 1.25                      | X                 |                       | L             |

`L` and `H` represent low denitrification and high denitrification, respectively, which are defined as the grids that
have low and high denitrification rates within the corn (2 years)-soybean-corn-hay (4 years) rotation or the corn
(4 years)-hay (4 years) rotation locations.

## Run

Run land surface hydrological spin-up using `run-Flux-PIHM.job`.

Cycles-L runs should be submitted using

```shell
sbatch --export=PROJECT=project ./run-Cycles-L.job
```

where `project` is the name of the simulation, i.e., scenario.
