# Cycles-L-WE38-simulation

Simulations using MM-PIHM version 1.0.0-rc3 (Cycles version 0.13.0-alpha).

## Scenarios

|Scenario                | Description |
|------------------------| ----------- |
|WE38                    | Modified from SWAT management file |
|WE38_1dot5xN            | 1.5x N application rate |

## Run

Run land surface hydrological spin-up using `run-Flux-PIHM.pbs`.

Cycles-L runs should be submitted using

```shell
qsub -v PROJECT=project run-Cycles-L.pbs
```

where `project` is the name of the simulation, i.e., scenario.
