# Verne2 

Verne2 is a fast, semi-analytic calculator for **Earth scattering** and **daily modulation** of **MeV-scale** dark matter. It implements straight-line propagation with screened dark-photon interactions and keeps the dominant scatter topologies (0, 1, or 2 elastic collisions) to build the **Transmitted** and **Reflected** components of the speed distribution at a detector.Verne2 is based on and extends **Verne** by Kavanagh to the MeV regime and screened dark-photon interactions. For the original formalism and WIMP/continuous-loss mode, see **https://github.com/bradkav/verne.git**.

Verne2 is based on and extends **Verne** by Kavanagh to the MeV regime and screened dark-photon interactions. For the original formalism and WIMP/continuous-loss mode, see [https://github.com/bradkav/verne](https://github.com/bradkav/verne)


## How to run a calculation (with `CalcVelDist_function.py`)

It computes the **speed distribution at the detector** for a given set of model and geometry parameters and (optionally) saves plots/arrays.

### 1) Minimal example (single angle)

```bash
python CalcVelDist_function.py \
  --mchi-mev 1.0 \
  --sigma-p 1e-30 \
  --mediator ulm \        # choices: ultralight (ulm) | heavy (hm)
  --gamma 0 \                    # isodetection angle 
  --depth-m 1000 \               # detector depth below surface
  --halo SHM \                   # Standard Halo Model params
  --out results

