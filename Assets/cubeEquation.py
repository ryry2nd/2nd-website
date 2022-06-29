from flask import Flask, render_template, request
import html

class CubeEquation:
    def __init__(self, app: Flask, prefix: str):
        self.prefix = prefix

        self.initCube(app)

    def initCube(self, app: Flask):
        @app.route("/cubeEquation", methods=["GET", "POST"])
        def cubeEquation():
            if request.method == "POST":
                try:
                    n = eval(request.form["row"])
                    intAns = int((0.5*(n-abs(n-2))+1)*n**2 + (n-2)*(n**2-(n-2)**2))
                    equation = f"parts=(0.5(({n:,g})-|({n:,g})-2|)+1)({n:,g})^2+(({n:,g})-2)(({n:,g})^2-(({n:,g})-2)^2)"
                    ans = f"parts={intAns:,g}"
                except (NameError, SyntaxError, ValueError):
                    equation = ""
                    ans = ""
            else:
                equation = ""
                ans = ""

            return render_template("cubeEquation.html", prefix=self.prefix, equation=equation, ans=ans)