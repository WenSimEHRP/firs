from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(
    id="liquids_terminal",
    accept_cargo_types=[],
    prod_cargo_types_with_multipliers=[],
    prob_in_game="2",
    prob_map_gen="6",
    map_colour="164",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_LIQUIDS_TERMINAL)",
    nearby_station_name="string(STR_STATION_TANK_FARM)",
    fund_cost_multiplier="152",
    override_default_construction_states=True,
    primary_production_random_factor_set="wide_range",
    sprites_complete=True,
)

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    accept_cargo_types=["EOIL", "OIL_"],
    prod_cargo_types_with_multipliers=[
        ("RFPR", 11),
        ("PETR", 7),
    ],
)
# industry.economy_variations['IN_A_HOT_COUNTRY'].prod_cargo_types_with_multipliers = [('NH3_', 16)]

industry.add_tile(
    id="liquids_terminal_tile_1",
    # we'll draw our own foundations as needed - this also conveniently adjusts the y offsets on the tile to where we want them
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    # supporting autoslope for the water tiles produces too many edge cases which are difficult to handle, so ban it
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="liquids_terminal_tile_2",
    # we'll draw our own foundations as needed - this also conveniently adjusts the y offsets on the tile to where we want them
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    # supporting autoslope for water tiles produces too many edge cases which are difficult to handle, so ban it
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)

sprite_ground = industry.add_sprite(sprite_number="GROUNDSPRITE_WATER")
spriteset_ground_empty = industry.add_spriteset(type="empty")
spriteset_small_tanks = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_office = industry.add_spriteset(
    sprites=[(440, 10, 64, 84, -31, -43)], zoffset=18
)
spriteset_spherical_tank = industry.add_spriteset(
    sprites=[(510, 10, 64, 84, -35, -61)],
)
spriteset_large_cylinder_tank = industry.add_spriteset(
    sprites=[(510, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_boat_1 = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -35, -15)],
)
spriteset_boat_2 = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -40, -12)],
)
spriteset_boat_3 = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -13, -19)],
)
spriteset_boat_4 = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -27, -12)],
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="liquids_terminal_spritelayout_coast_sphere_tank",
    tile="liquids_terminal_tile_2",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_spherical_tank,
            ],
            "sw": [
                spriteset_spherical_tank,
            ],
            "nw": [
                spriteset_spherical_tank,
            ],
            "ne": [
                spriteset_spherical_tank,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="liquids_terminal_spritelayout_small_tanks",
    tile="liquids_terminal_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_small_tanks,
            ],
            "sw": [
                spriteset_small_tanks,
            ],
            "nw": [
                spriteset_small_tanks,
            ],
            "ne": [
                spriteset_small_tanks,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="liquids_terminal_spritelayout_office",
    tile="liquids_terminal_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_office,
            ],
            "sw": [
                spriteset_office,
            ],
            "nw": [
                spriteset_office,
            ],
            "ne": [
                spriteset_office,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="liquids_terminal_spritelayout_large_tank",
    tile="liquids_terminal_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_large_cylinder_tank,
            ],
            "sw": [
                spriteset_large_cylinder_tank,
            ],
            "nw": [
                spriteset_large_cylinder_tank,
            ],
            "ne": [
                spriteset_large_cylinder_tank,
            ],
        },
    },
)

industry.add_spritelayout(
    id="liquids_terminal_spritelayout_water_barge_sw_ne",
    tile="liquids_terminal_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_1],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_barge_ne_sw",
    tile="liquids_terminal_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_2],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_water_barge_se_nw",
    tile="liquids_terminal_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_3],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_barge_nw_se",
    tile="liquids_terminal_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_4],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_water_empty",
    tile="liquids_terminal_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[],
)

industry.add_industry_jetty_layout(
    id="liquids_terminal_industry_layout_1",
    layout=[
        (0, 0, "liquids_terminal_spritelayout_large_tank"),
        (0, 1, "liquids_terminal_spritelayout_large_tank"),
        (0, 2, "liquids_terminal_spritelayout_water_empty"),
        (0, 3, "liquids_terminal_spritelayout_water_empty"),
        (0, 4, "spritelayout_null_water"),
        (1, 0, "liquids_terminal_spritelayout_large_tank"),
        (1, 1, "liquids_terminal_spritelayout_large_tank"),
        (1, 2, "liquids_terminal_spritelayout_large_tank"),
        (1, 3, "liquids_terminal_spritelayout_large_tank"),
        (1, 4, "spritelayout_null_water"),
        (2, 0, "liquids_terminal_spritelayout_large_tank"),
        (2, 1, "liquids_terminal_spritelayout_large_tank"),
        (2, 2, "liquids_terminal_spritelayout_water_empty"),
        (2, 3, "liquids_terminal_spritelayout_barge_nw_se"),
        (2, 4, "spritelayout_null_water"),
        (3, 0, "liquids_terminal_spritelayout_office"),
        (3, 1, "liquids_terminal_spritelayout_small_tanks"),
        (3, 2, "liquids_terminal_spritelayout_small_tanks"),
        (3, 3, "liquids_terminal_spritelayout_small_tanks"),
        (3, 4, "spritelayout_null_water"),
        (4, 0, "liquids_terminal_spritelayout_coast_sphere_tank"),
        (4, 1, "liquids_terminal_spritelayout_office"),
        (4, 2, "liquids_terminal_spritelayout_barge_ne_sw"),
        (4, 3, "liquids_terminal_spritelayout_water_empty"),
        (4, 4, "spritelayout_null_water"),
    ],
)

industry.add_industry_jetty_layout(
    id="liquids_terminal_industry_layout_2",
    layout=[
        (0, 0, "liquids_terminal_spritelayout_large_tank"),
        (0, 1, "liquids_terminal_spritelayout_large_tank"),
        (0, 2, "liquids_terminal_spritelayout_water_empty"),
        (0, 3, "liquids_terminal_spritelayout_water_empty"),
        (0, 4, "spritelayout_null_water"),
        (1, 0, "liquids_terminal_spritelayout_large_tank"),
        (1, 1, "liquids_terminal_spritelayout_large_tank"),
        (1, 2, "liquids_terminal_spritelayout_large_tank"),
        (1, 3, "liquids_terminal_spritelayout_large_tank"),
        (1, 4, "spritelayout_null_water"),
        (2, 0, "liquids_terminal_spritelayout_large_tank"),
        (2, 1, "liquids_terminal_spritelayout_large_tank"),
        (2, 2, "liquids_terminal_spritelayout_water_empty"),
        (2, 3, "liquids_terminal_spritelayout_barge_nw_se"),
        (2, 4, "spritelayout_null_water"),
        (3, 0, "liquids_terminal_spritelayout_office"),
        (3, 1, "liquids_terminal_spritelayout_small_tanks"),
        (3, 2, "liquids_terminal_spritelayout_small_tanks"),
        (3, 3, "liquids_terminal_spritelayout_small_tanks"),
        (3, 4, "spritelayout_null_water"),
        (4, 0, "liquids_terminal_spritelayout_coast_sphere_tank"),
        (4, 1, "liquids_terminal_spritelayout_office"),
        (4, 2, "liquids_terminal_spritelayout_barge_ne_sw"),
        (4, 3, "liquids_terminal_spritelayout_water_empty"),
        (4, 4, "spritelayout_null_water"),
    ],
)
