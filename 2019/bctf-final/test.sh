#!/usr/bin/env bash

# Author : Virink <virink@outlook.com>
# Date   : 2019/06/01, 01:14

URL="http://127.0.0.1:8080"

# POST
# /v1/flag/add	            map[POST:AddFlag]	    controllers.FlagController
# /v1/schedule/listdir	    map[POST:ListDir]	    controllers.ScheduleController
# /v1/settings/add	        map[POST:AddSettings]	controllers.SettingsController
# /v1/task/add	            map[POST:AddTask]	    controllers.TaskController
# /v1/user/login	        map[POST:Login]	        controllers.UserController
# /v1/user/logout	        map[POST:Logout]	    controllers.UserController
# GET
# /v1/flag/submitone	    map[GET:SubmitFlag]	    controllers.FlagController

# Login
curl -vv -s -X POST "$URL/v1/user/login" \
-H "Content-Type: application/json" \
-H "Cookie: beegosessionID=a0d3d904496f943310aa97cc6bf7743f" \
-d "{\"username\":\"admin\",\"password\":\"admin\",\"hint\":true}"

# submitone
# curl -vv -s "$URL/v1/flag/submitone" \
# -H "Content-Type: application/json" \
# -H "Cookie: beegosessionID=a0d3d904496f943310aa97cc6bf7743f" \
# -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0"

# Test
# curl -vv "$URL/v1/schedule/listdir" -d "dir=111"
echo
