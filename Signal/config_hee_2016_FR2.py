# Config file: options for signal fitting

_year = '2016'

signalScriptCfg = {
  
  # Setup
  'inputWSDir':'/vols/cms/jwd18/Hee/finalFits/CMSSW_10_2_13/src/flashggFinalFit/Signal/FullRun2/signal_2016',
  'procs':'auto', # if auto: inferred automatically from filenames
  'cats':'auto', # if auto: inferred automatically from (0) workspace
  'ext':'hee_%s'%_year,
  'analysis':'Hee', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py) and XSR info
  'year':'%s'%_year, # Use 'combined' if merging all years: not recommended
  'massPoints':'125',

  #Photon !shape! systematics
  'scales':'ElPtScale', # separate nuisance per year
  'scalesCorr':'', # correlated across years
  'scalesGlobal':'NonLinearity,Geant4', # affect all processes equally, correlated across years
  'smears':'', # separate nuisance per year

  # Job submission options
  'batch':'IC', # ['condor','SGE','IC','local']
  'queue':'hep.q'
  #'batch':'condor', # ['condor','SGE','IC','local']
  #'queue':'espresso',

}
