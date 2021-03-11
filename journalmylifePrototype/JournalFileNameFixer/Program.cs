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
                // fjerner alle control tegn fra strengen!
                string s = Regex.Replace(i, @"\p{C}+", string.Empty);
                //addListItem(i);
                // i = den orginale filnavn
                System.Console.WriteLine(i+i.Length);
                // s = den nye filnavn
                System.Console.WriteLine(s+s.Length);
                // if filename length != then rename file
                //if (!File.Exists(s))
                if((i+i.Length) != (s+s.Length)){
                    // unhandled System.IO.IOException  'En fil, som allerede findes, kan ikke oprettes.'
                    // if (!File.Exists(denFuldeSti))//denFuldeSti
                    if (!File.Exists(s)){
                        File.Move(i,s);
                    }                    
                }
            }
            // rename file names with U+200E
            // or rename if diffrent file/string length.
        }
    }
}
