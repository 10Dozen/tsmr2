
/* *********** This array defines detailed properties of zones ************************** */
[
	"forward_trench" /* Zone Name */
	,"EAST",true, /* Side, is Active */ [],[]
	/* Groups: */
	,[
		[
			1, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", ["entrenched"], "kit_syr_rat"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_rat"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_mg"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_rat"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_rat"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_rat"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_ar"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_at"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_ar"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_at"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_r"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_r"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_r"]
			]
		]
		,[
			1, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", ["indoors"], "kit_syr_random"]
				,["O_Soldier_F", ["indoors"], "kit_syr_random"]
				,["O_Soldier_F", ["indoors"], "kit_syr_random"]
				,["O_Soldier_F", ["indoors"], "kit_syr_random"]
				,["O_Soldier_F", ["indoors"], "kit_syr_random"]
				,["O_Soldier_F", ["indoors"], "kit_syr_random"]
				,["O_Soldier_F", ["indoors"], "kit_syr_random"]
				,["O_Soldier_F", ["indoors"], "kit_syr_random"]
			]
		]
	]
	/* Behavior: Speed, Behavior, Combat mode, Formation */
	,["FULL","SAFE","RED","WEDGE"]
]
,
[
	"bmp_stand" /* Zone Name */
	,"EAST",true, /* Side, is Active */ [],[]
	/* Groups: */
	,[
		[
			2, /* Groups quantity */
			/* Units */
			[
				["cwr3_o_bmp1", "Vehicle Hold", ""]
				,["O_Soldier_F", [0,"Commander"], "kit_syr_random"]
				,["O_Soldier_F", [0,"Gunner"], "kit_syr_random"]
				,["O_Soldier_F", [0,"Driver"], "kit_syr_random"]
			]
		]
	]
	/* Behavior: Speed, Behavior, Combat mode, Formation */
	,["FULL","COMBAT","RED","WEDGE"]
]
,
[
	"orchard" /* Zone Name */
	,"EAST",true, /* Side, is Active */ [],[]
	/* Groups: */
	,[
		[
			1, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", ["entrenched"], "kit_syr_r"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_mg"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_at"]
			]
		]
	]
	/* Behavior: Speed, Behavior, Combat mode, Formation */
	,["FULL","COMBAT","RED","WEDGE"]
]
,
[
	"rear_patrol" /* Zone Name */
	,"EAST",false, /* Side, is Active */ [],[]
	/* Groups: */
	,[
		[
			2, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", [], "kit_syr_ar"]
				,["O_Soldier_F", [], "kit_syr_gr"]
				,["O_Soldier_F", [], "kit_syr_rat"]
				,["O_Soldier_F", [], "kit_syr_at"]
			]
		]
		,[
			2, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", [], "kit_syr_r"]
				,["O_Soldier_F", [], "kit_syr_mg"]
				,["O_Soldier_F", [], "kit_syr_rat"]
				,["O_Soldier_F", [], "kit_syr_rat"]
			]
		]
	]
	/* Behavior: Speed, Behavior, Combat mode, Formation */
	,["FULL","COMBAT","RED","WEDGE"]
	 /* (OPTIONAL) Activation condition */
	,{ [ CHK_1, "east", "", "< 5"] call dzn_fnc_ccUnits OR [ CHK_2, "east", "", "< 5"] call dzn_fnc_ccUnits }
]
,
[
	"reinf_1" /* Zone Name */
	,"EAST",false, /* Side, is Active */ [],[]
	/* Groups: */
	,[
		[
			2, /* Groups quantity */
			/* Units */
			[
				["cwr3_o_bmp1", "Vehicle Advance", ""]
				,["O_Soldier_F", [0,"Commander"], "kit_syr_random"]
				,["O_Soldier_F", [0,"Gunner"], "kit_syr_random"]
				,["O_Soldier_F", [0,"Driver"], "kit_syr_random"]
				,["O_Soldier_F", [], "kit_syr_r"]
				,["O_Soldier_F", [], "kit_syr_at"]
				,["O_Soldier_F", [], "kit_syr_mg"]
				,["O_Soldier_F", [], "kit_syr_rat"]
				,["O_Soldier_F", [], "kit_syr_ar"]
				,["O_Soldier_F", [], "kit_syr_r"]
				,["O_Soldier_F", [], "kit_syr_rat"]
			]
		]
		,[
			2, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", [], "kit_syr_random"]
				,["O_Soldier_F", [], "kit_syr_random"]
				,["O_Soldier_F", [], "kit_syr_random"]
				,["O_Soldier_F", [], "kit_syr_random"]
			]
		]
	]
	/* Behavior: Speed, Behavior, Combat mode, Formation */
	,["FULL","COMBAT","RED","LINE"]
	 /* (OPTIONAL) Activation condition */
	,{ ([ TRG_1, "east", "", "< 5"] call dzn_fnc_ccUnits && [TRG_1, "", "> 1"] call dzn_fnc_ccPlayers) OR  ([ TRG_2, "east", "", "< 5"] call dzn_fnc_ccUnits && [TRG_2, "", "> 1"] call dzn_fnc_ccPlayers) }
]
,
[
	"forward_recce" /* Zone Name */
	,"EAST",true, /* Side, is Active */ [],[]
	/* Groups: */
	,[
		[
			3, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", [], "kit_syr_r"]
				,["O_Soldier_F", [], "kit_syr_rat"]
				,["O_Soldier_F", [], "kit_syr_rat"]
			]
		]
	]
	/* Behavior: Speed, Behavior, Combat mode, Formation */
	,["FULL","AWARE","RED","LINE"]
]
,
[
	"villa" /* Zone Name */
	,"EAST",true, /* Side, is Active */ [],[]
	/* Groups: */
	,[
		[
			3, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", [], "kit_syr_random"]
				,["O_Soldier_F", [], "kit_syr_random"]
				,["O_Soldier_F", [], "kit_syr_random"]
			]
		]
		,[
			1, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", ["entrenched"], "kit_syr_random"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_random"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_random"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_random"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_random"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_random"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_random"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_random"]
			]
		]
		,[
			1, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", ["indoors"], "kit_syr_random"]
				,["O_Soldier_F", ["indoors"], "kit_syr_random"]
				,["O_Soldier_F", ["indoors"], "kit_syr_random"]
				,["O_Soldier_F", ["indoors"], "kit_syr_random"]
			]
		]
	]
	/* Behavior: Speed, Behavior, Combat mode, Formation */
	,["FULL","COMBAT","RED","LINE"]
]
,
[
	"west_trench" /* Zone Name */
	,"EAST",true, /* Side, is Active */ [],[]
	/* Groups: */
	,[
		[
			1, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", ["entrenched"], "kit_syr_random"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_random"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_random"]
			]
		]
	]
	/* Behavior: Speed, Behavior, Combat mode, Formation */
	,["FULL","COMBAT","RED","LINE"]
]
,
[
	"main" /* Zone Name */
	,"EAST",true, /* Side, is Active */ [],[]
	/* Groups: */
	,[
		[
			2, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", [], "kit_syr_random"]
				,["O_Soldier_F", [], "kit_syr_random"]
				,["O_Soldier_F", [], "kit_syr_random"]
				,["O_Soldier_F", [], "kit_syr_random"]
			]
		]
	]
	/* Behavior: Speed, Behavior, Combat mode, Formation */
	,["FULL","COMBAT","RED","LINE"]
]
,
[
	"checkpoint" /* Zone Name */
	,"EAST",true, /* Side, is Active */ [],[]
	/* Groups: */
	,[
		[
			1, /* Groups quantity */
			/* Units */
			[
				["O_Soldier_F", ["entrenched"], "kit_syr_random"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_random"]
				,["O_Soldier_F", ["entrenched"], "kit_syr_random"]
			]
		]
	]
	/* Behavior: Speed, Behavior, Combat mode, Formation */
	,["FULL","COMBAT","RED","LINE"]
]
,
[
	"tank_reinf" /* Zone Name */
	,"EAST",false, /* Side, is Active */ [],[]
	/* Groups: */
	,[
		[
			1, /* Groups quantity */
			/* Units */
			[
				["cwr3_o_t55a", "Vehicle Patrol", ""]
				,["O_Soldier_F", [0,"Commander"], "kit_syr_crew"]
				,["O_Soldier_F", [0,"Gunner"], "kit_syr_crew"]
				,["O_Soldier_F", [0,"Driver"], "kit_syr_crew"]
			]
		]
	]
	/* Behavior: Speed, Behavior, Combat mode, Formation */
	,["FULL","COMBAT","RED","LINE"]
	 /* (OPTIONAL) Activation condition */
	,{ [ CHK_1, "east", "", "< 5"] call dzn_fnc_ccUnits && [CHK_2, "", "> 0"] call dzn_fnc_ccPlayers  }
]