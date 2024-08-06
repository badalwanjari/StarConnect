from base import app, db


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'app': app}

if __name__ == '__main__':
    app.run(debug=True)
