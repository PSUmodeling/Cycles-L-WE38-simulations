# Cycles-L-WE38-simulation

Simulations using MM-PIHM version 1.0.0-rc3 (Cycles version 0.13.0-alpha).

## Scenarios
|Scenario                | Description |
|------------------------| ----------- |
|WE38                    | Modified from SWAT management file |
|WE38_2ma                | Two manure applications per year |
|WE38_1dot5xN            | 1.5x N application rate |
|WE38_2ma_1dot5xN        | Two manure applications per year, 1.5x N application rate |
|WE38_2ma_1dot5xN_new    | Two manure applications per year, 1.5x N application rate, adjusted N application timing |
|WE38_2ma_1dot5xN_soil   | Two manure applications per year, 1.5x N application rate, adjusted soil types |

## Run
Jobs should be submitted using

```shell
qsub -v PROJECT=project run-PIHM.pbs
```

where `project` is the name of the simulation, i.e., scenario.
