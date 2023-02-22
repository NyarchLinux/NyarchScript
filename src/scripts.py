SCRIPTS = [
	{
		"title": "Updates",
		"icon-name": "audio-volume-high-symbolic",
		"sections": [
			{
			"title":  "Pacman",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Run full System Update",
						"subtitle": "Update the system and all of its packages",
						"command": "sudo pacman -Syu;exec bash",
						"description": "sudo pacman -Syu",
					},
					{
						"title": "Delete orphan packages",
						"subtitle": "Delete unutilized packages and dependencies that are not needed ",
						"command": "sudo pacman -Rs $ (pacman -Qtdq);exec bash",
						"description": "sudo pacman -Rs $ (pacman -Qtdq)",
					},
					{
						"title": "Refresh Keyring",
						"subtitle": "Refresh pacman Keyring, usually, it is very rarely needed",
						"command": "pacman-key --refresh-keys;exec bash",
						"description": "pacman-key --refresh-keys",
					},
				]
			}

		]
	},
	{
		"title": "Install",
		"icon-name": "audio-volume-high-symbolic",
		"sections": [
			{
			"title":  "Command-line Utilities",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Install fish",
						"subtitle": "This command installs fish and sets it as default shell",
						"command": "sudo pacman -S fish;exec bash",
						"description": "sudo pacman -S fish & chsh fish",
					},
				]
			},
			{
			"title":  "Themes",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Install GRUB theme",
						"subtitle": "This command installs fish and sets it as default shell",
						"command": "",
						"description": "",
					},
				]
			}
		]
	}








]
