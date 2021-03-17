# Config file: options for signal fitting

backgroundScriptCfg = {
  
  # Setup
  'inputWSDir':'/vols/cms/jwd18/Hee/finalFits/CMSSW_10_2_13/src/flashggFinalFit/Background/full_run_2_WSs', # location of 'allData.root' file
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'Hee_full_run_2', # extension to add to output directory
  'year':'combined', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'IC', # [condor,SGE,IC,local]
  'queue':'hep.q' # for condor e.g. microcentury
  
}
