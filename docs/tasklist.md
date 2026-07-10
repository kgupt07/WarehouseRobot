# Project tasklist

Track weekly deliverables and ops docs. Check off as you go.

---

## Week 2 — remaining (finish before Week 3)

- [ ] Reload saved map + AMCL (`warehouse_map.yaml`) — laser aligned after 2D Pose Estimate
- [ ] TF diagram → `docs/tf_tree.md` (`view_frames` + publisher labels)
- [ ] Write-up → `docs/mapping_vs_localization.md`
- [ ] **G3 blocker:** G2 must pass before starting Nav2 goals

---

## Week 2 — ops doc (backlog)

- [ ] **Document Gazebo spawn failure recovery** → `docs/troubleshooting_gazebo_spawn.md`
  - Symptom: world loads, no robot (empty Gazebo)
  - Cause: remote `spawn_entity` timed out or failed while Gazebo was still loading
  - Preconditions: `export TURTLEBOT3_MODEL=waffle_pi` in every terminal
  - Fix A: kill stale Gazebo, relaunch, wait 30–60 s before assuming failure
  - Fix B: manual spawn with `ros2 run gazebo_ros spawn_entity.py` (entity + SDF path)
  - Fix C: set `GAZEBO_MODEL_PATH` if model URI not found
  - Verify: `ros2 topic echo /scan --once` and `/odom` publish
  - Note: `navigation2.launch.py` does **not** spawn the robot — run sim first

---

## Week 3 — Autonomous Navigation (~24–28 h)

**Gate G3:** Nav2 reaches one goal reliably in RViz.

**Prerequisite:** Week 2 complete (map loads, AMCL + initial pose works).

### Deliverables

- [ ] G3: Single Nav2 goal in RViz succeeds
- [ ] Three poses in sequence (A → B → C)
- [ ] Home + search poses recorded in `docs/poses.md`
- [ ] Python node: NavigateToPose to home and search area
- [ ] Chain: go to search → wait → go home (no camera yet)

### Concepts to learn

- Nav2 stack (planner, controller, behavior tree, recovery)
- Global vs local costmaps
- `NavigateToPose` action (not a topic)
- Why mission code sends goals, not `/cmd_vel`

### Step-by-step (high level)

#### Part 1 — First autonomous goal (~6–8 h)

1. Terminal 1: Gazebo sim (robot visible)
2. Terminal 2: Navigation with your map + `use_sim_time:=true`
3. RViz: Fixed Frame = `map`, Map + LaserScan + TF
4. 2D Pose Estimate — laser on walls
5. Add Nav2 Goal plugin (or use toolbar **Nav2 Goal** / **2D Goal Pose**)
6. Click a goal in open space; watch global plan + robot drive
7. If it fails: read terminal for costmap / planner errors; try closer goal

#### Part 2 — Understand Nav2 (~4–6 h)

1. `ros2 node list` — identify planner, controller, behavior server, AMCL, map_server
2. Skim TurtleBot 3 nav params (robot radius, max velocity)
3. Trigger a recovery (block path briefly) — observe spin / backup
4. Reflection: global planner vs local controller vs costmap

#### Part 3 — Record poses (~2 h)

1. Drive robot to home location (teleop or Nav2)
2. Read pose from RViz or `ros2 topic echo /amcl_pose`
3. Fill `docs/poses.md` (home + search, map frame)
4. Pick a third pose (B) for A → B → C drill

#### Part 4 — Three goals in a row (~4–6 h)

1. Initial pose
2. Nav2 goal A → wait for success
3. Goal B → success
4. Goal C → success
5. Note any recovery behaviors; repeat until reliable

#### Part 5 — Python NavigateToPose (~6–8 h)

1. ROS 2 action client tutorial (Humble)
2. Node in `mission_robot`: send goal to `/navigate_to_pose`
3. Hardcode or parametrize home + search from `docs/poses.md`
4. Run: navigate to search → sleep → navigate home
5. **Do not** publish `/cmd_vel` from mission node — Nav2 owns motion

### Common Week 3 mistakes

- Nav2 launched without sim / without initial pose
- Goal placed inside obstacle or outside map
- Custom map missing free space (`0` cells) — use demo map if needed
- Mission node fighting Nav2 on `/cmd_vel`
- Forgot `use_sim_time:=true`

### Reflection (before Week 4)

- Global planner vs local controller?
- Should your mission node publish `/cmd_vel`? Why or why not?
- What happens if AMCL loses localization mid-navigation?

### Risk

Highest-risk week. Budget 2 extra debug sessions. If stuck >2 sessions, use default TurtleBot map and stock nav launch unmodified.

---

## Week 4 — preview (after G3)

- Camera / ArUco detection
- Mission state machine: HOME → SEARCH → DETECT → REPORT → GO_HOME
- Publish `/mission/target_found`
- Full end-to-end mission once

See `docs/ros_robot_project_plan.html` for full Week 4 detail.
