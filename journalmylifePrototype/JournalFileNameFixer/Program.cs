using System;
using System.IO;
using System.Text.RegularExpressions;

namespace JournalFileNameFixer
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string winDir = System.Environment.GetEnvironmentVariable("windir");

            //string[] files = Directory.GetFiles(winDir);
            string[] files = Directory.GetFiles("..");
            foreach (string i in files)
            {
                string s = Regex.Replace(i, @"\p{C}+", string.Empty);
                //addListItem(i);
                System.Console.WriteLine(i+i.Length);
                System.Console.WriteLine(s+s.Length);

            }
            // rename file names with U+200E
            // or rename if diffrent file/string length.
        }
    }
}
