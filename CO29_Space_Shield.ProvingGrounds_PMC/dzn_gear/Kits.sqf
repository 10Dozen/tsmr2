// ***********************************
// Gear Kits 
// ***********************************
// ******** GEAR CLASSES **********
//
//	Maptools		"ACE_MapTools"	["ACE_MapTools",1]
//	Binocular		"Binocular"	["Binocular",1]		
//
// 	Map			"ItemMap"
//	Compass			"ItemCompass"
//	Watch			"ItemWatch"
//	Personal Radio		"ItemRadio"
//
// ******* KIT NAMES FORMAT ********
//  Kit names format:		kit_FACTION_ROLE
//	Platoon Leader / Командир Взвода	->	kit_ussf_pl
//	Squad Leader / Командир отделения	->	kit_ussf_sl
//	Section Leader				->	kit_ussf_sl
//	2IC					->	kit_ussf_2ic
//	Fireteam Leader				->	kit_ussf_ftl
//	Automatic Rifleman			->	kit_ussf_ar
//	Grenadier / Стрелок (ГП)		->	kit_ussf_gr
//	Rifleman / Стрелок			->	kit_ussf_r
//	Экипаж					->	kit_ussf_crew
//	Пулеметчик				->	kit_ussf_mg
//	Стрелок-Гранатометчик			->	kit_ussf_at
//	Стрелок, помощник гранатометчика	->	kit_ussf_aat
//	Старший стрелок				->	kit_ussf_ar / kit_ussf_ss
//	Снайпер					->	kit_ussf_mm
// ****************
//
// ******** USEFUL MACROSES *******
// Maros for Empty weapon
#define EMPTYKIT	[["","","","",""],["","","","",""],["","","","",""],["","","","",""],[],[["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0],["",0]],[["",0],["",0],["",0],["",0],["",0],["",0]],[]]
// Macros for Empty weapon
#define EMPTYWEAPON	"","",["","","",""]
// Macros for the list of items to be chosen randomly
#define RANDOM_ITEM	["H_HelmetB_grass","H_HelmetB"]
// Macros to give the item only if daytime is in given inerval (e.g. to give NVGoggles only at night)
#define NIGHT_ITEM(X)	if (daytime < 9 || daytime > 18) then { X } else { "" }

// ******** ASSIGNED and UNIFORM ITEMS MACRO ********
#define NVG_NIGHT_ITEM		if (daytime < 9 || daytime > 18) then { "CUP_NVG_GPNVG_black" } else { "" }
#define BINOCULAR_ITEM		"Binocular"

#define ASSIGNED_ITEMS		"ItemMap","ItemCompass","ItemWatch","ItemRadio","ItemGPS", NVG_NIGHT_ITEM
#define ASSIGNED_ITEMS_L	"ItemMap","ItemCompass","ItemWatch","ItemRadio","ItemGPS", NVG_NIGHT_ITEM, BINOCULAR_ITEM

#define UNIFORM_ITEMS		["ACE_fieldDressing",5],["ACE_packingBandage",5],["ACE_elasticBandage",5],["ACE_tourniquet",2],["ACE_morphine",2],["ACE_epinephrine",2],["ACE_quikclot",5],["ACE_CableTie",2],["ACE_Flashlight_XL50",1],["ACE_EarPlugs",1]
#define UNIFORM_ITEMS_L		["ACE_fieldDressing",5],["ACE_packingBandage",5],["ACE_elasticBandage",5],["ACE_tourniquet",2],["ACE_morphine",2],["ACE_epinephrine",2],["ACE_quikclot",5],["ACE_CableTie",2],["ACE_Flashlight_XL50",1],["ACE_EarPlugs",1],["ACE_MapTools",1]
// ****************

kit_uru_r = [
	["<EQUIPEMENT >>  ","TRYK_U_Bts_UCP_PCUs","rhsusf_spcs_ucp_teamleader_alt","CUP_B_US_IIID_UCP","CUP_H_OpsCore_Covered_UCP_SF","CUP_PMC_Facewrap_Black"],
	["<PRIMARY WEAPON >>  ","CUP_arifle_AK103","CUP_30Rnd_762x39_AK103_bakelite_M",["CUP_muzzle_Bizon","acc_flashlight","CUP_optic_1p63",""]],
	["<LAUNCHER WEAPON >>  ","CUP_launch_RPG7V","CUP_PG7VL_M",["","","CUP_optic_PGO7V",""]],
	["<HANDGUN WEAPON >>  ","CUP_hgun_Glock17","CUP_17Rnd_9x19_glock17",["muzzle_snds_L","acc_flashlight_pistol","optic_MRD",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["PRIMARY MAG",10],["SmokeShell",2],["CUP_HandGrenade_RGD5",3]]],
	["<BACKPACK ITEMS >> ",[["SECONDARY MAG",3],["HANDGUN MAG",5]]]
];
kit_uru_gr = [
	["<EQUIPEMENT >>  ","TRYK_U_Bts_UCP_PCUs","rhsusf_spcs_ucp_teamleader_alt","CUP_B_US_IIID_UCP","CUP_H_OpsCore_Covered_UCP_SF","CUP_PMC_Facewrap_Black"],
	["<PRIMARY WEAPON >>  ","CUP_arifle_AK103_GL","CUP_30Rnd_762x39_AK103_bakelite_M",["CUP_muzzle_Bizon","acc_flashlight","CUP_optic_1p63",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","CUP_hgun_Glock17","CUP_17Rnd_9x19_glock17",["muzzle_snds_L","acc_flashlight_pistol","optic_MRD",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["SmokeShell",2],["CUP_HandGrenade_RGD5",3],["PRIMARY MAG",10]]],
	["<BACKPACK ITEMS >> ",[["HANDGUN MAG",5],["CUP_1Rnd_HE_GP25_M",15],["CUP_1Rnd_SMOKE_GP25_M",5],["CUP_1Rnd_SmokeRed_GP25_M",5]]]
];
kit_uru_ar = [
	["<EQUIPEMENT >>  ","TRYK_U_Bts_UCP_PCUs","rhsusf_spcs_ucp_teamleader_alt","CUP_B_US_IIID_UCP","CUP_H_OpsCore_Covered_UCP_SF","CUP_PMC_Facewrap_Black"],
	["<PRIMARY WEAPON >>  ","CUP_lmg_minimi_railed","CUP_200Rnd_TE4_Red_Tracer_556x45_M249",["muzzle_snds_M","","",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","CUP_hgun_Glock17","CUP_17Rnd_9x19_glock17",["muzzle_snds_L","acc_flashlight_pistol","optic_MRD",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["SmokeShell",2],["CUP_HandGrenade_RGD5",3],["PRIMARY MAG",2]]],
	["<BACKPACK ITEMS >> ",[["HANDGUN MAG",5],["PRIMARY MAG",3]]]
];
kit_uru_ftl = [
	["<EQUIPEMENT >>  ","TRYK_U_Bts_UCP_PCUs","rhsusf_spcs_ucp_teamleader_alt","CUP_B_US_IIID_UCP","CUP_H_OpsCore_Covered_UCP_SF","CUP_PMC_Facewrap_Black"],
	["<PRIMARY WEAPON >>  ","CUP_arifle_AK103","CUP_30Rnd_762x39_AK103_bakelite_M",["CUP_muzzle_Bizon","acc_pointer_IR","CUP_optic_1p63",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","CUP_hgun_Glock17","CUP_17Rnd_9x19_glock17",["muzzle_snds_L","acc_flashlight_pistol","optic_MRD",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["SmokeShell",2],["CUP_HandGrenade_RGD5",3],["PRIMARY MAG",10]]],
	["<BACKPACK ITEMS >> ",[["HANDGUN MAG",5]]]
];
kit_uru_pl = [
	["<EQUIPEMENT >>  ","TRYK_U_Bts_UCP_PCUs","rhsusf_spcs_ucp_teamleader_alt","TFAR_rt1523g_black","CUP_H_OpsCore_Covered_UCP_SF","CUP_PMC_Facewrap_Black"],
	["<PRIMARY WEAPON >>  ","CUP_arifle_AK103","CUP_30Rnd_762x39_AK103_bakelite_M",["CUP_muzzle_Bizon","acc_pointer_IR","CUP_optic_1p63",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","CUP_hgun_Glock17","CUP_17Rnd_9x19_glock17",["muzzle_snds_L","acc_flashlight_pistol","optic_MRD",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["SmokeShell",2],["CUP_HandGrenade_RGD5",3],["PRIMARY MAG",10]]],
	["<BACKPACK ITEMS >> ",[["HANDGUN MAG",5]]]
];
kit_uru_sl = [
	["<EQUIPEMENT >>  ","TRYK_U_Bts_UCP_PCUs","rhsusf_spcs_ucp_teamleader_alt","TFAR_rt1523g_black","CUP_H_OpsCore_Covered_UCP_SF","CUP_PMC_Facewrap_Black"],
	["<PRIMARY WEAPON >>  ","CUP_arifle_AK103","CUP_30Rnd_762x39_AK103_bakelite_M",["CUP_muzzle_Bizon","acc_pointer_IR","CUP_optic_1p63",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","CUP_hgun_Glock17","CUP_17Rnd_9x19_glock17",["muzzle_snds_L","acc_flashlight_pistol","optic_MRD",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["SmokeShell",2],["CUP_HandGrenade_RGD5",3],["PRIMARY MAG",10]]],
	["<BACKPACK ITEMS >> ",[["HANDGUN MAG",5]]]
];
kit_uru_psgt = [
	["<EQUIPEMENT >>  ","TRYK_U_Bts_UCP_PCUs","rhsusf_spcs_ucp_teamleader_alt","TFAR_rt1523g_black","CUP_H_OpsCore_Covered_UCP_SF","CUP_PMC_Facewrap_Black"],
	["<PRIMARY WEAPON >>  ","CUP_arifle_AK103","CUP_30Rnd_762x39_AK103_bakelite_M",["CUP_muzzle_Bizon","acc_pointer_IR","CUP_optic_1p63",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","CUP_hgun_Glock17","CUP_17Rnd_9x19_glock17",["muzzle_snds_L","acc_flashlight_pistol","optic_MRD",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["SmokeShell",2],["CUP_HandGrenade_RGD5",3],["PRIMARY MAG",10]]],
	["<BACKPACK ITEMS >> ",[["HANDGUN MAG",5]]]
];


kit_ino_r = [
	["<EQUIPEMENT >>  ","U_O_Protagonist_VR","V_I_G_resistanceLeader_F","B_FieldPack_ocamo","H_RacingHelmet_4_F",""],
	["<PRIMARY WEAPON >>  ","arifle_Mk20_plain_F","30Rnd_556x45_Stanag",["","","ACE_optic_Arco_2D",""]],
	["<LAUNCHER WEAPON >>  ","launch_B_Titan_short_F","Titan_AT",["","","",""]],
	["<HANDGUN WEAPON >>  ","hgun_Pistol_heavy_01_F","11Rnd_45ACP_Mag",["hlc_muzzle_Octane45","hlc_acc_TLR1","HLC_optic_RomeoV",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["PRIMARY MAG",10],["rhs_mag_m67",1],["SmokeShell",2]]],
	["<BACKPACK ITEMS >> ",[["SECONDARY MAG",1],["HANDGUN MAG",5],["Titan_AP",1]]]
];
kit_ino_gr = [
	["<EQUIPEMENT >>  ","U_O_Protagonist_VR","V_I_G_resistanceLeader_F","B_FieldPack_ocamo","H_RacingHelmet_4_F",""],
	["<PRIMARY WEAPON >>  ","arifle_Mk20_GL_plain_F","30Rnd_556x45_Stanag",["","","ACE_optic_Arco_2D",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","hgun_Pistol_heavy_01_F","11Rnd_45ACP_Mag",["hlc_muzzle_Octane45","hlc_acc_TLR1","HLC_optic_RomeoV",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["rhs_mag_m67",1],["SmokeShell",2],["PRIMARY MAG",10]]],
	["<BACKPACK ITEMS >> ",[["HANDGUN MAG",5],["CUP_1Rnd_HEDP_M203",10],["CUP_1Rnd_HE_M203",5],["CUP_1Rnd_Smoke_M203",5],["CUP_1Rnd_SmokeRed_M203",5]]]
];
kit_ino_ftl = [
	["<EQUIPEMENT >>  ","U_O_Protagonist_VR","V_I_G_resistanceLeader_F","B_FieldPack_ocamo","H_RacingHelmet_4_F",""],
	["<PRIMARY WEAPON >>  ","arifle_Mk20_plain_F","30Rnd_556x45_Stanag",["","","ACE_optic_Arco_2D",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","hgun_Pistol_heavy_01_F","11Rnd_45ACP_Mag",["hlc_muzzle_Octane45","hlc_acc_TLR1","HLC_optic_RomeoV",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["rhs_mag_m67",1],["SmokeShell",2],["PRIMARY MAG",10]]],
	["<BACKPACK ITEMS >> ",[["HANDGUN MAG",5]]]
];
kit_ino_pl = [
	["<EQUIPEMENT >>  ","U_O_Protagonist_VR","V_I_G_resistanceLeader_F","TFAR_mr6000l","H_RacingHelmet_4_F",""],
	["<PRIMARY WEAPON >>  ","arifle_Mk20_plain_F","30Rnd_556x45_Stanag",["","","ACE_optic_Arco_2D",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","hgun_Pistol_heavy_01_F","11Rnd_45ACP_Mag",["hlc_muzzle_Octane45","hlc_acc_TLR1","HLC_optic_RomeoV",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["rhs_mag_m67",1],["SmokeShell",2],["PRIMARY MAG",10]]],
	["<BACKPACK ITEMS >> ",[["HANDGUN MAG",2]]]
];
kit_ino_sl = [
	["<EQUIPEMENT >>  ","U_O_Protagonist_VR","V_I_G_resistanceLeader_F","TFAR_mr6000l","H_RacingHelmet_4_F",""],
	["<PRIMARY WEAPON >>  ","arifle_Mk20_plain_F","30Rnd_556x45_Stanag",["","","ACE_optic_Arco_2D",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","hgun_Pistol_heavy_01_F","11Rnd_45ACP_Mag",["hlc_muzzle_Octane45","hlc_acc_TLR1","HLC_optic_RomeoV",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["rhs_mag_m67",1],["SmokeShell",2],["PRIMARY MAG",10]]],
	["<BACKPACK ITEMS >> ",[["HANDGUN MAG",2]]]
];
kit_ino_psgt = [
	["<EQUIPEMENT >>  ","U_O_Protagonist_VR","V_I_G_resistanceLeader_F","TFAR_mr6000l","H_RacingHelmet_4_F",""],
	["<PRIMARY WEAPON >>  ","arifle_Mk20_plain_F","30Rnd_556x45_Stanag",["","","ACE_optic_Arco_2D",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","hgun_Pistol_heavy_01_F","11Rnd_45ACP_Mag",["hlc_muzzle_Octane45","hlc_acc_TLR1","HLC_optic_RomeoV",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["rhs_mag_m67",1],["SmokeShell",2],["PRIMARY MAG",10]]],
	["<BACKPACK ITEMS >> ",[["HANDGUN MAG",2]]]
];
kit_ino_ar = [
	["<EQUIPEMENT >>  ","U_O_Protagonist_VR","V_I_G_resistanceLeader_F","","H_RacingHelmet_4_F",""],
	["<PRIMARY WEAPON >>  ","arifle_MX_SW_Black_F","100Rnd_65x39_caseless_black_mag",["","","ACE_optic_Arco_2D","bipod_01_F_blk"]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","hgun_Pistol_heavy_01_F","11Rnd_45ACP_Mag",["hlc_muzzle_Octane45","hlc_acc_TLR1","HLC_optic_RomeoV",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["rhs_mag_m67",1],["SmokeShell",2],["100Rnd_65x39_caseless_black_mag_tracer",3]]],
	["<BACKPACK ITEMS >> ",[]]
];

kit_ino_random = [
   "kit_ino_r"
   ,"kit_ino_gr"
   ,"kit_ino_ar"
   ,"kit_ino_ftl"
   ,"kit_ino_pl"
   ,"kit_ino_sl"
   ,"kit_ino_psgt"
];

kit_ino_crew = [
	["<EQUIPEMENT >>  ","U_O_Protagonist_VR","V_I_G_resistanceLeader_F","","H_RacingHelmet_4_F",""],
	["<PRIMARY WEAPON >>  ","","",["","","",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","hgun_Pistol_heavy_01_F","11Rnd_45ACP_Mag",["hlc_muzzle_Octane45","hlc_acc_TLR1","HLC_optic_RomeoV",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["rhs_mag_m67",1],["SmokeShell",2],["HANDGUN MAG",5]]],
	["<BACKPACK ITEMS >> ",[]]
];


cargo_kit_landRover = [
	[["CUP_hgun_Glock17",3],["CUP_arifle_AK103",2],["CUP_launch_RPG7V",2]],
	[["CUP_30Rnd_762x39_AK103_bakelite_M",15],["SmokeShell",15],["CUP_HandGrenade_RGD5",15],["CUP_17Rnd_9x19_glock17",15],["CUP_200Rnd_TE4_Red_Tracer_556x45_M249",1],["CUP_PG7VL_M",5],["CUP_1Rnd_SmokeRed_GP25_M",15],["CUP_1Rnd_HE_GP25_M",15],["CUP_1Rnd_SMOKE_GP25_M",15]],
	[["ACE_rope6",1],["ACE_packingBandage",30],["ACE_fieldDressing",30],["ACE_elasticBandage",30],["ACE_quikclot",30],["ACE_morphine",20],["ACE_CableTie",30],["ACE_tourniquet",30],["ACE_epinephrine",20]],
	[["CUP_B_US_IIID_UCP",5]]
];