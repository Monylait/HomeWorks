using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using System.Threading.Tasks;



namespace Calc_1

{

    class Class1

    {

        public double Logicl_work(double X, double Y, string Z)

        {

            double Res = 0;

            if (Z == "+")

            {

                Res = X + Y;

            }

            else if (Z == "-")

            {

                Res = X - Y;

            }

            else if (Z == "*")

            {

                Res = X * Y;

            }

            else if (Z == "/")

            {

                if (Y == 0)

                    Res = 0;

                else

                    Res = X / Y;

            }

            else if (Z == "^")

            {

                Res = Math.Pow(X, Y);

            }

            else if (Z == "Sq")

            {

                Res = Math.Sqrt(X);

            }

            return Res;

        }

    }

}