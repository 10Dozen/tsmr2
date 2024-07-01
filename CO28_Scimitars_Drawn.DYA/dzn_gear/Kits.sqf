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
#define NVG_NIGHT_ITEM		if (daytime < 9 || daytime > 18) then { "CUP_NVG_PVS14" } else { "" }
#define BINOCULAR_ITEM		"Binocular"

#define ASSIGNED_ITEMS		"ItemMap","ItemCompass","ItemWatch"
#define ASSIGNED_ITEMS_L	"ItemMap","ItemCompass","ItemWatch","ItemRadio", BINOCULAR_ITEM
#define ASSIGNED_ITEMS_UK	"ItemMap","ItemCompass","ItemWatch", NVG_NIGHT_ITEM
#define ASSIGNED_ITEMS_UK_L	"ItemMap","ItemCompass","ItemWatch","ItemRadio", BINOCULAR_ITEM, NVG_NIGHT_ITEM

#define UNIFORM_ITEMS		["ACE_fieldDressing",5],["ACE_packingBandage",5],["ACE_elasticBandage",5],["ACE_tourniquet",2],["ACE_morphine",2],["ACE_epinephrine",2],["ACE_quikclot",5],["ACE_CableTie",2],["ACE_Flashlight_XL50",1],["ACE_EarPlugs",1]
#define UNIFORM_ITEMS_L		["ACE_fieldDressing",5],["ACE_packingBandage",5],["ACE_elasticBandage",5],["ACE_tourniquet",2],["ACE_morphine",2],["ACE_epinephrine",2],["ACE_quikclot",5],["ACE_CableTie",2],["ACE_Flashlight_XL50",1],["ACE_EarPlugs",1],["ACE_MapTools",1]
// ****************

#define UK_UNI ["CUP_U_B_BDUv2_dirty_DDPM","CUP_U_B_BDUv2_DDPM","CUP_U_B_BDUv2_gloves_DDPM","CUP_U_B_BDUv2_gloves_dirty_DDPM","CUP_U_B_BDUv2_roll2_DDPM","CUP_U_B_BDUv2_roll_gloves_dirty_DDPM","CUP_U_B_BDUv2_roll_gloves_DDPM"]
#define UK_HEAD ["CUP_H_BAF_DDPM_Mk6_EMPTY","CUP_H_BAF_DDPM_Mk6_NETTING_PRR","CUP_H_BAF_DDPM_Mk6_GLASS_PRR"]

kit_uk_r = [
	["<EQUIPEMENT >>  ",UK_UNI,"CUP_V_B_BAF_DDPM_Osprey_Mk3_Rifleman","CUP_B_Bergen_BAF",UK_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_L85A2","CUP_30Rnd_556x45_Stanag_L85",["","","CUP_optic_SUSAT",""]],
	["<LAUNCHER WEAPON >>  ","CUP_launch_M136_Loaded","CUP_M136_M",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_UK],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["CUP_HandGrenade_L109A1_HE",5],["PRIMARY MAG",16]]],
	["<BACKPACK ITEMS >> ",[["ACE_wirecutter",1],["ACE_Clacker",1],["PRIMARY MAG",1],["CUP_100Rnd_TE4_LRT4_Red_Tracer_762x51_Belt_M",3],["DemoCharge_Remote_Mag",3]]]
];
kit_uk_mg = [
	["<EQUIPEMENT >>  ",UK_UNI,"CUP_V_B_BAF_DDPM_Osprey_Mk3_Rifleman","CUP_B_Bergen_BAF",UK_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_lmg_L7A2_Flat","CUP_100Rnd_TE4_LRT4_Red_Tracer_762x51_Belt_M",["","","",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_UK],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["CUP_HandGrenade_L109A2_HE",2],["PRIMARY MAG",3]]],
	["<BACKPACK ITEMS >> ",[["PRIMARY MAG",6],["CUP_H_BAF_DPM_Mk6_EMPTY",1]]]
];
kit_uk_mm = [
	["<EQUIPEMENT >>  ",UK_UNI,"CUP_V_B_BAF_DDPM_Osprey_Mk3_AutomaticRifleman","CUP_B_Bergen_BAF",UK_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_L86A2","CUP_30Rnd_556x45_Stanag_L85",["","","CUP_optic_SUSAT_PIP",""]],
	["<LAUNCHER WEAPON >>  ","CUP_launch_M136_Loaded","CUP_M136_M",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_UK],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["CUP_HandGrenade_L109A2_HE",4],["PRIMARY MAG",16]]],
	["<BACKPACK ITEMS >> ",[["PRIMARY MAG",5]]]
];
kit_uk_ftl = [
	["<EQUIPEMENT >>  ",UK_UNI,"CUP_V_B_BAF_DDPM_Osprey_Mk3_Rifleman","CUP_B_Bergen_BAF",UK_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_L85A2_GL","CUP_30Rnd_556x45_Stanag_L85",["","","CUP_optic_SUSAT_PIP",""]],
	["<LAUNCHER WEAPON >>  ","CUP_launch_M136_Loaded","CUP_M136_M",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_UK_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["PRIMARY MAG",14],["CUP_1Rnd_HE_M203",12],["CUP_HandGrenade_L109A2_HE",2]]],
	["<BACKPACK ITEMS >> ",[["PRIMARY MAG",8],["CUP_1Rnd_HE_M203",5],["SmokeShellBlue",3],["SmokeShell",2]]]
];
kit_uk_sl = [
	["<EQUIPEMENT >>  ",UK_UNI,"CUP_V_B_BAF_DDPM_Osprey_Mk3_Officer","usm_pack_st138_prc77",UK_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_L85A2","CUP_30Rnd_556x45_Stanag_L85",["","","CUP_optic_SUSAT",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_UK_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["CUP_HandGrenade_L109A2_HE",4],["PRIMARY MAG",15]]],
	["<BACKPACK ITEMS >> ",[["PRIMARY MAG",6],["SmokeShellBlue",2],["SmokeShell",2],["SmokeShellRed",2],["ACE_HandFlare_Green",2]]]
];
kit_uk_gr = [
	["<EQUIPEMENT >>  ","CUP_U_B_BDUv2_roll_gloves_DDPM","CUP_V_B_BAF_DDPM_Osprey_Mk3_Grenadier","CUP_B_Bergen_BAF",UK_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_L85A2_GL","CUP_30Rnd_556x45_Stanag_L85",["","","CUP_optic_SUSAT",""]],
	["<LAUNCHER WEAPON >>  ","CUP_launch_M136_Loaded","CUP_M136_M",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_UK],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["PRIMARY MAG",14],["CUP_1Rnd_HE_M203",12],["CUP_HandGrenade_L109A2_HE",2]]],
	["<BACKPACK ITEMS >> ",[["PRIMARY MAG",3],["CUP_200Rnd_TE4_Red_Tracer_556x45_L110A1",2]]]
];
kit_uk_ar = [
	["<EQUIPEMENT >>  ","CUP_U_B_BDUv2_roll_gloves_DDPM","CUP_V_B_BAF_DDPM_Osprey_Mk3_AutomaticRifleman","CUP_B_Bergen_BAF","CUP_H_BAF_DDPM_Mk6_GLASS_PRR",""],
	["<PRIMARY WEAPON >>  ","CUP_lmg_L110A1","CUP_200Rnd_TE4_Red_Tracer_556x45_L110A1",["","","CUP_optic_SUSAT",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_UK],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["PRIMARY MAG",4],["CUP_HandGrenade_L109A2_HE",5]]],
	["<BACKPACK ITEMS >> ",[["PRIMARY MAG",3]]]
];
kit_uk_pl = [
	["<EQUIPEMENT >>  ","CUP_U_B_BDUv2_dirty_DDPM","CUP_V_B_BAF_DDPM_Osprey_Mk3_Officer","usm_pack_st138_prc77","CUP_H_BAF_DDPM_Mk6_EMPTY",""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_L85A2","CUP_30Rnd_556x45_Stanag_L85",["","","CUP_optic_SUSAT_PIP",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_UK_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["CUP_HandGrenade_L109A2_HE",4],["PRIMARY MAG",15],["SmokeShellBlue",2],["SmokeShellPurple",2],["SmokeShellYellow",1]]],
	["<BACKPACK ITEMS >> ",[["SmokeShellGreen",2],["SmokeShellRed",2],["SmokeShellYellow",2],["SmokeShellBlue",2]]]
];
kit_uk_crew = [
	["<EQUIPEMENT >>  ","CUP_U_B_BDUv2_roll2_DDPM","CUP_V_B_BAF_DDPM_Osprey_Mk3_Crewman","","cwr3_b_headgear_cvc",""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_L85A2","CUP_30Rnd_556x45_Stanag_L85",["","","CUP_optic_SUSAT_PIP",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_UK_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS_L]],
	["<VEST ITEMS >> ",[["PRIMARY MAG",5],["ACE_HandFlare_Green",2],["ACE_HandFlare_Red",1],["CUP_HandGrenade_L109A2_HE",1],["SmokeShellBlue",2],["SmokeShellPurple",2]]],
	["<BACKPACK ITEMS >> ",[]]
];
cargo_kit_uk = [
	[["CUP_arifle_L85A2",4],["CUP_launch_M136_Loaded",5]],
	[["CUP_M136_M",5],["SmokeShell",4],["SmokeShellOrange",4],["Chemlight_red",4],["CUP_30Rnd_556x45_Stanag_L85",40],["CUP_200Rnd_TE4_Red_Tracer_556x45_L110A1",15],["CUP_HandGrenade_L109A2_HE",15]],
	[["FirstAidKit",10],["ACE_rope12",1]],
	[["CUP_B_Bergen_BAF",8]]
];
#define SYR_UNI ["cwr3_b_fia_uniform_woodland","cwr3_b_fia_uniform_woodland_olive","cwr3_b_fia_uniform_woodland_olive_rolled","cwr3_b_fia_uniform_woodland_rolled"]
#define SYR_HEAD ["CUP_H_SLA_Helmet_DES","CUP_H_SLA_Helmet_DES_worn","cwr3_b_headgear_cap_m81_sf_woodland","cwr3_o_headgear_ssh68_net"]

kit_syr_random = [
	"kit_syr_r"
	,"kit_syr_r"
	,"kit_syr_r"
	,"kit_syr_r"
	,"kit_syr_at"
	,"kit_syr_at"
	,"kit_syr_r"
	,"kit_syr_ar"
	,"kit_syr_at"
	,"kit_syr_rat"
	,"kit_syr_gr"
	,"kit_syr_grat"
	,"kit_syr_rat"
	,"kit_syr_rat"
	,"kit_syr_rat"
	,"kit_syr_mm"
];
kit_syr_r = [
	["<EQUIPEMENT >>  ",SYR_UNI,"cwr3_o_vest_chicom_beltkit_ak74","",SYR_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_AKM","CUP_30Rnd_762x39_AK47_bakelite_M",["","","",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["PRIMARY MAG",11],["CUP_HandGrenade_RGD5",1]]],
	["<BACKPACK ITEMS >> ",[]]
];
kit_syr_mg = [
	["<EQUIPEMENT >>  ",SYR_UNI,"cwr3_o_vest_chicom_beltkit_ak74","cwr3_o_backpack_gasmask",SYR_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_lmg_PKM","CUP_100Rnd_TE4_LRT4_762x54_PK_Tracer_Green_M",["","","",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["CUP_HandGrenade_RGD5",1],["PRIMARY MAG",2]]],
	["<BACKPACK ITEMS >> ",[["PRIMARY MAG",2]]]
];
kit_syr_ar = [
	["<EQUIPEMENT >>  ",SYR_UNI,"cwr3_o_vest_chicom_beltkit_ak74","cwr3_o_backpack_gasmask",SYR_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_RPK74","CUP_75Rnd_TE4_LRT4_Green_Tracer_762x39_RPK_M",["","","",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["CUP_HandGrenade_RGD5",1],["PRIMARY MAG",5]]],
	["<BACKPACK ITEMS >> ",[["PRIMARY MAG",4]]]
];
kit_syr_at = [
	["<EQUIPEMENT >>  ",SYR_UNI,"cwr3_o_vest_chicom_beltkit_ak74","cwr3_o_backpack_rpg7",SYR_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_AKMS_Early","CUP_30Rnd_762x39_AK47_bakelite_M",["","","",""]],
	["<LAUNCHER WEAPON >>  ","CUP_launch_RPG7V","CUP_PG7VL_M",["","","CUP_optic_PGO7V3",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["CUP_HandGrenade_RGD5",1],["PRIMARY MAG",11]]],
	["<BACKPACK ITEMS >> ",[["SECONDARY MAG",2]]]
];
kit_syr_rat = [
	["<EQUIPEMENT >>  ",SYR_UNI,"cwr3_o_vest_chicom_beltkit_ak74","",SYR_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_AKM","CUP_30Rnd_762x39_AK47_bakelite_M",["","","",""]],
	["<LAUNCHER WEAPON >>  ","CUP_launch_RPG18_Loaded","CUP_RPG18_M",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["PRIMARY MAG",11],["CUP_HandGrenade_RGD5",1]]],
	["<BACKPACK ITEMS >> ",[]]
];
kit_syr_gr = [
	["<EQUIPEMENT >>  ",SYR_UNI,"cwr3_o_vest_chicom_beltkit_gl","",SYR_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_AKM_GL_Early","CUP_30Rnd_762x39_AK47_bakelite_M",["","","",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["CUP_HandGrenade_RGD5",1],["PRIMARY MAG",11],["CUP_1Rnd_HE_GP25_M",6]]],
	["<BACKPACK ITEMS >> ",[]]
];
kit_syr_grat = [
	["<EQUIPEMENT >>  ",SYR_UNI,"cwr3_o_vest_chicom_beltkit_gl","",SYR_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_AKM_GL_Early","CUP_30Rnd_762x39_AK47_bakelite_M",["","","",""]],
	["<LAUNCHER WEAPON >>  ","CUP_launch_RPG18_Loaded","CUP_RPG18_M",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["CUP_HandGrenade_RGD5",1],["PRIMARY MAG",11],["CUP_1Rnd_HE_GP25_M",6]]],
	["<BACKPACK ITEMS >> ",[]]
];
kit_syr_mm = [
	["<EQUIPEMENT >>  ",SYR_UNI,"cwr3_o_vest_chicom_beltkit_ak74","",SYR_HEAD,""],
	["<PRIMARY WEAPON >>  ","CUP_srifle_SVD","CUP_10Rnd_762x54_SVD_M",["","","CUP_optic_PSO_1",""]],
	["<LAUNCHER WEAPON >>  ","CUP_launch_RPG18_Loaded","CUP_RPG18_M",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS_L],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["PRIMARY MAG",16]]],
	["<BACKPACK ITEMS >> ",[]]
];
kit_syr_crew = [
	["<EQUIPEMENT >>  ","cwr3_b_fia_uniform_woodland_rolled","cwr3_o_vest_chicom_beltkit_gl","","cwr3_o_headgear_tsh3",""],
	["<PRIMARY WEAPON >>  ","CUP_arifle_AKS74U","CUP_30Rnd_545x39_AK74_plum_M",["","","",""]],
	["<LAUNCHER WEAPON >>  ","","",["","","",""]],
	["<HANDGUN WEAPON >>  ","","",["","","",""]],
	["<ASSIGNED ITEMS >>  ", ASSIGNED_ITEMS],
	["<UNIFORM ITEMS >> ",[UNIFORM_ITEMS]],
	["<VEST ITEMS >> ",[["CUP_30Rnd_545x39_AK_M",4]]],
	["<BACKPACK ITEMS >> ",[]]
];
