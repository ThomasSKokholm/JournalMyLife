using System;

namespace NewJournalTemplate
{
    // New Journal File template
    // 
    // 1 (start)
    // 2  [tt:mm] [DD-MM-YYYY]
    // 3 Journal_[Dag] Den [DD]. [month] [YYYY]
    // ... indhold...
    // (EOF) (slut)
    //    [tt:mm] [DD-MM-YYYY]
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("New Journal file maker in C# .Net!");
            // get datetime
            // Fra https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings
            DateTime thisDate1 = new DateTime(2011, 6, 10);
            Console.WriteLine("Today is " + thisDate1.ToString("MMMM dd, yyyy") + ".");

            DateTimeOffset thisDate2 = new DateTimeOffset(2011, 6, 10, 15, 24, 16,
                                              TimeSpan.Zero);
            Console.WriteLine("The current date and time: {0:MM/dd/yy H:mm:ss zzz}", thisDate2);

            Console.WriteLine("{0}", thisDate1);

            // format time string
            // format date string.
            // inset time and date string in fileContent template.
            // formate new journal-filename
            // open new journal file
            //      streamReader
            // save file content
            // close file.
        }
    }
}
