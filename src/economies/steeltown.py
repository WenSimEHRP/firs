from economy import Economy
economy = Economy(id = "STEELTOWN",
                  numeric_id = 5,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'acid',
                            'mail',
                            'carbon_black',
                            'cast_iron',
                            'cement',
                            'chlorine',
                            'vehicles', # no goods?
                            'coal',
                            'coke',
                            'electrical_machines',
                            'food',
                            'engineering_supplies',
                            'farm_supplies',
                            'glass',
                            'iron_ore',
                            'limestone',
                            'lye',
                            'manganese',
                            'oxygen',
                            'pig_iron',
                            'petrol',
                            'pipe',
                            'plastics',
                            'quicklime',
                            'rubber',
                            'salt',
                            'sand',
                            'scrap_metal',
                            'slag',
                            'soda_ash',
                            'steel',
                            'sulphur',
                            'coal_tar',
                            'tyres',
                            'vehicle_bodies',
                            'vehicle_engines',
                            'vehicle_parts',
                            'zinc'])
