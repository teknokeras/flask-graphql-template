from flask_app import create_app

if __name__ == '__main__':
	app = create_app()
	app.run(threaded=True, debug=True, host='0.0.0.0', port=8080)