# gemMask
```bash
cmsrel CMSSW_11_2_4
cd CMSSW_11_2_4/src
cmsenv
git clone https://github.com/jshlee/gemMask
cd gemMask
```

You can edit the end of gemdetit.py to produce a list of strips to mask and save it to deadMask.dat or hotMask.dat
```bash
python3 gemdetit.py
```

once deadMask.dat or hotMask.dat is made run reconstruction process, step_3_cfg.py with input file of choice (using /RelValZMM_14/CMSSW_11_2_0-PU_112X_mcRun3_2021_realistic_v14-v1/GEN-SIM-DIGI-RAW in this example)
```bash
cmsRun step_3_cfg.py
```
