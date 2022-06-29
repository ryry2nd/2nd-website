from flask import Flask, render_template, request
import html

class CubeEquation:
    def __init__(self, app: Flask, prefix: str):
        self.prefix = prefix

        self.initCube(app)
    
    def initCube(self, app: Flask):
        @app.route("/cubeEquation/", methods=["GET", "POST"])
        def cubeEquation():
            if request.method == "POST":
                n = int(request.form["row"])
                equation = f"parts=2({n})^2+(({n})-2)(({n})^2-(({n})-2)^2)"
                ans = f"parts={2*(n**2)+(n-2)*(n**2-(n-2)**2)}"
            else:
                equation = ""
                ans = ""

            return render_template("cubeEquation.html", prefix=self.prefix, equation=equation, ans=ans)