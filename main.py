from flask import Flask, request, jsonify
import the_2048

app = Flask(__name__)

# Initialize the game state
matrix = the_2048.start_game()

@app.route("/", methods=["GET", "POST"])
def main():
    global matrix
    
    if request.method == "POST":
        key = request.json.get("key")
        
        if key == "up":  
            the_2048.move_up(matrix)
        elif key == "down": 
            the_2048.move_down(matrix)
        elif key == "left":
            the_2048.left(matrix)
        elif key == "right": 
            the_2048.right(matrix)
        else:
            return jsonify({"error": "Invalid input"})
            
        status = the_2048.current_state(matrix)
        response = {"matrix": matrix, "status": status}
        
        if status != 'Not over':
            response["message"] = "You lost!"
        elif status == 'You won!':
            response["message"] = "You won!"
        else:
            the_2048.add_two(matrix)
            
        return jsonify(response)
    
    return jsonify(matrix)

if __name__ =='__main__':
    app.run(debug=True, port=5500)
