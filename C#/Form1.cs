using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;




namespace Calc_1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            textBox2.Text = "0";
            textBox3.Text = "0";
        }

        private double? First = null, Second=null,Global=null,M=null;
        private int result = 0,Z=0;
        string operation="", operation_2="";
        int start = 0, Dot=0;
        Class1 myClass = new Class1();

        private void button18_Click(object sender, EventArgs e)
        {
            if (First == null)
            {
                First = Convert.ToDouble(textBox2.Text);
                textBox3.Text = First.ToString();
            }
            else if ((Second == null) && (operation != ""))
            {
                Second = Convert.ToDouble(textBox2.Text);
            }
            textBox2.Clear();
            textBox2.Text = "0";
            if (operation == "")
            {
                operation = "^";
            }
            else
            {
                operation_2 = "^";
            }
            if ((First != null) && (Second != null) && (operation != ""))
            {
                First = myClass.Logicl_work((double)First, (double)Second, operation);
                textBox3.Text = First.ToString();
                operation = operation_2;
                Second = null;
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            textBox2.Clear();
            textBox2.Text = "0";
            textBox3.Clear();
            textBox3.Text = "Sq";
            if (operation == "")
            {
                operation = "Sq";
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            string txt = textBox2.Text;
            if ((txt.Length == 1) || (txt.Length == 0))
                textBox2.Text = "0";
            else
            {
                txt = txt.Substring(0, txt.Length - 1);
                textBox2.Text = txt;
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            textBox2.Text="0";
            textBox3.Text = "0";
            First = null;
            Second = null;
            operation = "";
            operation_2 = "";
            result = 0;
            M = null;
            Dot = 0;
        }
        //=
        private void button14_Click(object sender, EventArgs e)
        {
            if (operation != "Sq")
            {
                if (Second == null)
                    Second = Convert.ToDouble(textBox2.Text);
                if ((First != null) && ((Second != null)||(Second != 0)) && (operation != ""))
                {
                    First = myClass.Logicl_work((double)First, (double)Second, operation);
                    textBox3.Text = First.ToString();
                    operation = operation_2="";
                    Second = null;

                }
            }
            else
            {
                First = Convert.ToDouble(textBox2.Text);
                if (First != 0)
                {
                    First = myClass.Logicl_work((double)First, 0, operation);
                    textBox3.Text = First.ToString();
                    operation = operation_2 = "";
                    Second = null;
                }
            }
            textBox2.Text = "0";
        }
        private void button23_Click(object sender, EventArgs e)
        {
            string loc= Convert.ToString(textBox2.Text);
            int indexOfChar = loc.IndexOf(",");
            if (indexOfChar == -1)
            {
                textBox2.Text += ",";
                Dot = 1;
            }
        }
        private void button24_Click(object sender, EventArgs e)
        {
            double loc = Convert.ToDouble(textBox2.Text);
            M = M + loc;
        }

        private void button25_Click(object sender, EventArgs e)
        {
            double loc = Convert.ToDouble(textBox2.Text);
            M = M - loc;
        }

        private void button22_Click(object sender, EventArgs e)
        {
            M = null;
        }
        private void button21_Click(object sender, EventArgs e)
        {
            double loc = Convert.ToDouble(textBox3.Text);
            if (loc != 0) 
            { 
                M = Convert.ToDouble(textBox3.Text); 
            }
        }
        private void button20_Click(object sender, EventArgs e)
        {
            if ((M!=null)&&(operation!=""))
            {
                textBox2.Text = M.ToString();
                M = null;
            }
        }
        private void button19_Click(object sender, EventArgs e)
        {
            if (First == null)
            {
                First = Convert.ToDouble(textBox2.Text);
                textBox3.Text = First.ToString();
            }
            else if ((Second == null) && (operation != ""))
            {
                Second = Convert.ToDouble(textBox2.Text);
            }
            textBox2.Clear();
            textBox2.Text = "0";
            if (operation == "")
            {
                operation = "/";
            }
            else
            {
                operation_2 = "/";
            }
            if ((First != null) && (Second != null) && (operation != ""))
            {
                First = myClass.Logicl_work((double)First, (double)Second, operation);
                textBox3.Text = First.ToString();
                operation = operation_2;
                Second = null;
            }
        }
        //*
        private void button13_Click(object sender, EventArgs e)
        {
            if (First == null)
            {
                First = Convert.ToDouble(textBox2.Text);
                textBox3.Text = First.ToString();
            }
            else if ((Second == null) && (operation != ""))
            {
                Second = Convert.ToDouble(textBox2.Text);
            }
            textBox2.Clear();
            textBox2.Text = "0";
            if (operation == "")
            {
                operation = "*";
            }
            else
            {
                operation_2 = "*";
            }
            if ((First != null) && (Second != null) && (operation != ""))
            {
                First = myClass.Logicl_work((double)First, (double)Second, operation);
                textBox3.Text = First.ToString();
                operation = operation_2;
                Second = null;
            }
        }
        //-
        private void button12_Click(object sender, EventArgs e)
        {
            if (First == null)
            {
                First = Convert.ToDouble(textBox2.Text);
            }
            else if ((Second==null)&& (operation != ""))
            {
                Second = Convert.ToDouble(textBox2.Text);
            }
            textBox2.Clear();
            textBox2.Text = "0";
            if (operation == "")
            {
                operation = "-";
            }
            else
            {
                operation_2 = "-";
            }
            if ((First != null) && (Second != null) && (operation != ""))
            {
                First = myClass.Logicl_work((double)First, (double)Second, operation);
                textBox3.Text = First.ToString();
                operation = operation_2;
                Second = null;
            }
        }

//+
        private void button11_Click(object sender, EventArgs e)
        {
            if (First==null)
            {
                First= Convert.ToDouble(textBox2.Text);
                textBox3.Text = First.ToString();
            }
            else if ((Second == null) && (operation != ""))
            {
                Second = Convert.ToDouble(textBox2.Text);
            }
            textBox2.Text = "0";
            if (operation=="")
            {
                operation = "+";
            }
            else
            {
                operation_2 = "+";
            }
            if ((First!=null)&&(Second!=null)&&(operation!=""))
                {
                First= myClass.Logicl_work((double)First, (double)Second, operation);
                textBox3.Text = First.ToString();
                operation = operation_2;
                Second = null;
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            if (result == 1)
            {
                textBox2.Clear();
                result = 0;
            }

            double loc = Convert.ToDouble(textBox2.Text);
            if (loc == 0)
                textBox2.Clear();
            textBox2.Text += "0";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            if (result == 1)
            {
                textBox2.Clear();
                result = 0;
            }
            double loc = Convert.ToDouble(textBox2.Text);
            if (loc == 0)
                textBox2.Clear();
            textBox2.Text += "9";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (result == 1)
            {
                textBox2.Clear();
                result = 0;
            }
            double loc = Convert.ToDouble(textBox2.Text);
            if (loc == 0)
                textBox2.Clear();
            textBox2.Text += "8";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (result == 1)
            {
                textBox2.Clear();
                result = 0;
            }
            double loc = Convert.ToDouble(textBox2.Text);
            if (loc == 0)
                textBox2.Clear();
            textBox2.Text += "7";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (result == 1)
            {
                textBox2.Clear();
                result = 0;
            }
            double loc = Convert.ToDouble(textBox2.Text);
            if (loc == 0)
                textBox2.Clear();
            textBox2.Text += "6";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (result == 1)
            {
                textBox2.Clear();
                result = 0;
            }
            double loc = Convert.ToDouble(textBox2.Text);
            if (loc == 0)
                textBox2.Clear();
            textBox2.Text += "5";
        }


        private void button4_Click(object sender, EventArgs e)
        {
            if (result == 1)
            {
                textBox2.Clear();
                result = 0;
            }
            double loc = Convert.ToDouble(textBox2.Text);
            if (loc == 0)
                textBox2.Clear();
            textBox2.Text += "4";
        }


        private void button3_Click(object sender, EventArgs e)
        {
            if (result == 1)
            {
                textBox2.Clear();
                result = 0;
            }
            double loc = Convert.ToDouble(textBox2.Text);
            if (loc == 0)
                textBox2.Clear();
            textBox2.Text += "3";
        }


        private void button2_Click(object sender, EventArgs e)
        {
            if (result == 1)
            {
                textBox2.Clear();
                result = 0;
            }
            double loc = Convert.ToDouble(textBox2.Text);
            if (loc == 0)
                textBox2.Clear();
            textBox2.Text += "2";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (result == 1)
            {
                textBox2.Clear();
                result = 0;
            }
            double loc = Convert.ToDouble(textBox2.Text);
            if (loc == 0)
                textBox2.Clear();
            textBox2.Text += "1";
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }
    }

}



//TextBox1.clear
