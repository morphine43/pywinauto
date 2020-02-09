using System.Drawing;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Text = "Form1";
        }
        private void InitializeComponent(uint itemsCount, uint rowCount = 1)
        {
            this.components = new System.ComponentModel.Container();
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Text = "Form1";
            uint colCount = itemsCount / rowCount;
            if (itemsCount % rowCount != 0)
            {
                colCount++;
            }

            for (uint i = 0; i < itemsCount; i++)
            {
                var label = new Label();
                label.AutoSize = false;
                label.Text = "Label " + (i + 1);

                var txt = new TextBox();
                txt.Text = "TextBox " + (i + 1);

                label.AutoSize = false;
                SizeF extent = TextRenderer.MeasureText(label.Text, label.Font);
                label.Width = (int)extent.Width;

                txt.AutoSize = false;
                extent = TextRenderer.MeasureText(txt.Text, txt.Font);
                txt.Width = (int)extent.Width;

                int height = label.Height;
                if (height < txt.Height)
                {
                    height = txt.Height;
                }
                int width = label.Width + txt.Width;

                label.Top = (int)(i % colCount) * height;
                label.Left = (int)(i / colCount) * width;
                txt.Top = label.Top;
                txt.Left = label.Right;
                this.Controls.Add(label);
                this.Controls.Add(txt);
            }

            this.AutoScroll = true;
        }
        #endregion
    }
}

