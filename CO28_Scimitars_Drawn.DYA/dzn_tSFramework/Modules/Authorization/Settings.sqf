#include "data\script_component.hpp"
/* Dependency:  No
 */

#define ARTILLERY_ALLOWED true
#define AIRBORNE_ALLOWED true
#define POM_ALLOWED true
#define ARTILLERY_NO false
#define AIRBORNE_NO false
#define POM_NO false
#define ALL_ALLOWED true,true,true
#define ARTILLERY_ONLY_ALLOWED true,false,false
#define ARTY_AND_AIRBORNE_ALLOWED true,true,false

/*
 *	List of Authorized roles in format:
 *		ROLE (@Role description) HAS [@Artillery_Permission, @Airborne_Permission, @POM_Permission] PERMISSIONS
 *
 *	, where:
 *		@Role description - <STRING> unit's role description (partial search, so 1'1 Squad Leader will match "Squad Leader"). 
 *							Special are: "Admin" (logged in admin), "Any" - every player
 *		@Artillery_Permission - <BOOLEAN> true if allowed, false if not
 *		@Airborne_Permission - <BOOLEAN> true if allowed, false if not
 *		@POM_Permission - <BOOLEAN> true if allowed, false if not
 */

GVAR(RuleList) = [

	ROLE "Admin"					HAS [ALL_ALLOWED] PERMISSIONS,
	ROLE "1'0 Platoon Leader@1'0" HAS [ALL_ALLOWED] PERMISSIONS,
	ROLE "Platoon Sergeant" HAS [ALL_ALLOWED] PERMISSIONS,
	ROLE "1'1 Section Leader@1'1" HAS [ARTILLERY_ALLOWED] PERMISSIONS,
	ROLE "1'2 Section Leader@1'2" HAS [ARTILLERY_ALLOWED] PERMISSIONS,
	ROLE "1'3 Section Leader@1'3" HAS [ARTILLERY_ALLOWED] PERMISSIONS
];
