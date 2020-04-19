from economy import Economy
economy = Economy(id = "BETTER_LIVING_THROUGH_CHEMISTRY",
                  numeric_id = 2,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'acid',
                            'mail',
                            'alcohol',
                            'aluminium',
                            'ammonia',
                            'ammonium_nitrate',
                            'cement',
                            'chlorine',
                            'clay',
                            'cleaning_agents',
                            'food', # must be in slot 11
                            'coal',
                            'coal_tar',
                            'coke',
                            'copper',
                            'electrical_parts',
                            'engineering_supplies',
                            'ethylene',
                            'farm_supplies',
                            'fish',
                            'food_additives',
                            'furniture',
                            'glass',
                            'grain',
                            'iron_ore',
                            'limestone',
                            'livestock',
                            'lumber',
                            'lye',
                            'milk',
                            'naphtha',
                            'oil',
                            'oxygen',
                            'packaging',
                            'paints_and_coatings',
                            'petrol',
                            'phosphate',
                            'phosphoric_acid',
                            'plant_fibres', # should be cotton?
                            'plastics',
                            'potash',
                            'rubber', # includes synthetic rubber, export only
                            'salt',
                            'sand',
                            'soda_ash',
                            'steel',
                            'stone',
                            #'sugar', # import?
                            'sulphur',
                            'textiles',
                            'tinplate',
                            'urea',
                            'vehicles',
])
