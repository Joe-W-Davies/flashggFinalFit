# Input config file for running trees2ws

trees2wsCfg = {

  # Name of RooDirectory storing input tree
  'inputTreeDir':'',

  # Variables to be added to dataframe: use wildcard * for common strings
  'mainVars':["CMS_hgg_mass","weight","dZ","centralObjectWeight","*sigma","qcd_scale_variation*"], # Var for the nominal RooDataSets #NOTE: nominal weight systs #FIXME
  'dataVars':["CMS_hgg_mass","weight"], # Vars to be added for data
  'stxsVar':'',
  'notagVars':["weight"], # Vars to add to NOTAG RooDataset
  'systematicsVars':["CMS_hgg_mass","weight"], # Variables to add to sytematic RooDataHists
  'theoryWeightContainers':{},

  # List of systematics: use string YEAR for year-dependent systematics #NOTE: for separate trees
  #'systematics':['jer', 'jesTotal', 'ElPtScale'],
  'systematics':['jer', 'jesTotal', 'NonLinearity','EBHighR9ElPtScale', 'EBLowR9ElPtScale', 'EEHighR9ElPtScale', 'EELowR9ElPtScale'],

  # Analysis categories: python list of cats or use 'auto' to extract from input tree
  'cats':'auto'

}
