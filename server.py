from flask import Flask, request, jsonify
from robodk import robolink, robomath
import threading
import time

# -----------------------------
# Flask setup
# -----------------------------
app = Flask(__name__)
RDK = robolink.Robolink()  # Connect to RoboDK

# Get references (update names as per your station)
conveyor = RDK.Item('Conveyor Belt (2m)', robolink.ITEM_TYPE_FRAME)
robot = RDK.Item('R1', robolink.ITEM_TYPE_ROBOT)
carton_ref = RDK.Item('Carton Template', robolink.ITEM_TYPE_OBJECT)  # Template carton


# -----------------------------
# Endpoint: Start Conveyor
# -----------------------------
@app.route('/start_conveyor', methods=['POST'])
def start_conveyor():
    def routine():
        print("🟢 Conveyor Run triggered from Unity")
        prog = RDK.Item('Conveyor Run', robolink.ITEM_TYPE_PROGRAM)
        if not prog.Valid():
            print("❌ Conveyor Run program not found in RoboDK")
            return
        prog.RunProgram()
        print("✅ Conveyor movement complete")
    threading.Thread(target=routine).start()
    return jsonify({'status': 'Conveyor Run started'})




# -----------------------------
# Endpoint: Spawn Carton
# -----------------------------
@app.route('/spawn_carton', methods=['POST'])
def spawn_carton():
    print("\n[DEBUG] Spawn carton called...")

    # Step 1: Check connection
    print("[DEBUG] Checking RoboDK connection...")
    if not RDK.Connected():
        return jsonify({'error': 'RoboDK not connected! Open RoboDK before running the server.'}), 500

    # Step 2: Check items in RoboDK
    all_items = RDK.ItemList()
    print(f"[DEBUG] Items in RoboDK station: {all_items}")

    # Step 3: Try to get your carton template
    carton_ref = RDK.Item("Carton Template")
    if not carton_ref.Valid():
        return jsonify({
            'error': 'Carton Template not found!',
            'items_found': all_items
        }), 404

    print("[DEBUG] Found Carton Template:", carton_ref.Name())

    # Step 4: Try to copy it
    carton_clone = RDK.Copy(carton_ref)
    print("[DEBUG] Copy result:", carton_clone)

    if carton_clone is None or not carton_clone.Valid():
        return jsonify({'error': 'RDK.Copy() failed to duplicate the item'}), 500

    # Step 5: Assign name and pose
    clone_name = f"Carton_{int(time.time())}"
    carton_clone.setName(clone_name)
    carton_clone.setPose(carton_ref.Pose())

    print("[DEBUG] Successfully created", clone_name)
    return jsonify({'status': 'Carton spawned', 'name': clone_name})


# -----------------------------
# Endpoint: Delete Carton
# -----------------------------
@app.route('/delete_carton', methods=['POST'])
def delete_carton():
    data = request.get_json()
    name = data.get('name', None)

    print(f"\n[SERVER] Received request to delete carton: {name}")

    if not name:
        print("[ERROR] Missing 'name' field in JSON.")
        return jsonify({'error': 'Missing "name" field in JSON'}), 400

    # Make sure name is treated as a string
    carton = RDK.Item(str(name), robolink.ITEM_TYPE_OBJECT)

    if not carton.Valid():
        print(f"[ERROR] No carton named {name} found in RoboDK.")
        return jsonify({'error': f'No item named {name} found'}), 404

    carton.Delete()
    print(f"[SERVER] 🗑️ Deleted carton: {name}")
    return jsonify({'status': f'{name} deleted successfully'})

# -----------------------------
# Endpoint: Pick & Place
# -----------------------------
@app.route('/pick_place', methods=['POST'])
def pick_place():
    try:
        prog = RDK.Item('Pick_Place')
        if not prog.Valid():
            return jsonify({"error": "Program 'Pick_Place' not found in RoboDK"}), 404
        prog.RunProgram()
        return jsonify({"status": "Pick and place started"})
    except Exception as e:
        print("❌ Error while running pick_place:", str(e))
        return jsonify({"error": str(e)}), 500
@app.route('/Pick_Place', methods=['POST'])
def pick_place_upper():
    return pick_place()


# -----------------------------
# Endpoint: Robot pose
# -----------------------------
@app.route('/get_pose', methods=['GET'])
def get_pose():
    robot = RDK.Item('R1', robolink.ITEM_TYPE_ROBOT)  # ⚠️ Replace 'UR5e' with your robot's exact name in RoboDK
    if not robot.Valid():
        return jsonify({'error': 'Robot not found'}), 404

    pose = robot.Pose()
    pos = pose.Pos()  # [x, y, z] in mm

    return jsonify({
        'x': pos[0],
        'y': pos[1],
        'z': pos[2]
    })

# -----------------------------
# Endpoint: Robot joints
# -----------------------------
@app.route('/get_joints', methods=['GET'])
def get_joints():
    robot = RDK.Item('R1', robolink.ITEM_TYPE_ROBOT)  # replace with your robot name
    if not robot.Valid():
        return jsonify({'error': 'Robot not found'}), 404

    joints = robot.Joints().tolist()  # [j1, j2, j3, j4, j5, j6] in degrees
    return jsonify({'joints': joints})


# -----------------------------
# (Optional) Endpoint: Safety or Status Check
# -----------------------------
@app.route('/status', methods=['GET'])
def status():
    return jsonify({'robot_connected': robot.Valid(), 'station': RDK.getParam('PATH_OPENSTATION')})


# -----------------------------
# Run Server
# -----------------------------
if __name__ == '__main__':
    print("✅ RoboDK Flask server running at http://127.0.0.1:5000")

    print("📋 Available programs:")
    for item in RDK.ItemList(robolink.ITEM_TYPE_PROGRAM):
        print("-", item.Name())

    app.run(host='127.0.0.1', port=5000)
