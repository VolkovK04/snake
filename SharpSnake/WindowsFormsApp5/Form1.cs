using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        int time = 0;
        async void foo()
        {
            string host = "192.168.43.19";
            int port = 9090;
            var socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            //try
            //{
            await socket.ConnectAsync(host, port);
            //MessageBox.Show($"Подключение к {socket.RemoteEndPoint} установлено");
            while (true)
            {
                // определяем отправляемые данные
                var message = $"0 {curse}";
                // конвертируем данные в массив байтов
                var messageBytes = Encoding.UTF8.GetBytes(message);
                // отправляем данные
                await socket.SendAsync(new ArraySegment<byte>(messageBytes), SocketFlags.None);
                // буфер для получения данных
                var responseBytes = new ArraySegment<byte>(new byte[900]);
                // получаем данные
                var bytes = await socket.ReceiveAsync(responseBytes, SocketFlags.None);
                //// преобразуем полученные данные в строку
                //string response = Encoding.UTF8.GetString(responseBytes.Array, 0, bytes);
                //// выводим данные на консоль
                //Console.WriteLine(response);
                DrawMap(mapFromBytes(responseBytes.Array));
                label1.Text = time.ToString();
                time++;
            }

            //}
            //catch (SocketException)
            //{
            //    Console.WriteLine($"Не удалось установить подключение с {socket.RemoteEndPoint}");
            //}
            MessageBox.Show("End");
        }
        static int mapSize = 30;
        int[,] mapFromBytes(byte[] bytes)
        {
            int[,] map = new int[30, 30];
            int counter = 0;
            for (int i = 0; i < mapSize; i++)
            {
                for (int j = 0; j < mapSize; j++)
                {
                    map[i, j] = bytes[counter];
                    counter++;
                }
            }
            return map;
        }
        void DrawMap(int[,] map)
        {
            Bitmap img = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(img);
            g.Clear(Color.White);
            for (int i = 0; i < mapSize; i++)
            {
                for (int j = 0; j < mapSize; j++)
                {
                    DrawCell(g, i, j, map[i, j]);
                }
            }
            pictureBox1.Image = img;
            img.Save($"img{time}.png");
        }
        void DrawCell(Graphics g, int x, int y, int type)
        {
            int CELL_SIZE = 10;
            Color color = Color.Black;
            switch (type)
            {
                case 0:
                    {
                        color = Color.White;
                        break;
                    }
                case 1:
                    {
                        color = Color.Red;
                        break;
                    }
                case 2:
                    {
                        color = Color.Green;
                        break;
                    }
                case 3:
                    {
                        color = Color.Brown;
                        break;
                    }

            }
            Rectangle rect = new Rectangle(CELL_SIZE * x, CELL_SIZE * y, CELL_SIZE, CELL_SIZE);
            g.FillRectangle(new SolidBrush(color), rect);
            g.DrawRectangle(new Pen(Color.Black), rect);
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            foo();
        }
        int curse = 0;
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            Keys keys = e.KeyCode;
            switch (keys)
            {
                case Keys.W:
                    {
                        curse = 0;
                        break;
                    }
                case Keys.D:
                    {
                        curse = 1;
                        break;
                    }
                case Keys.S:
                    {
                        curse = 2;
                        break;
                    }
                case Keys.A:
                    {
                        curse = 3;
                        break;
                    }
            }
        }
    }
}
