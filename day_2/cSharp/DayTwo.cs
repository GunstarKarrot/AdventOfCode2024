using System;

namespace DayTwo
{
    public class Program
    {
        /// <summary>
        /// Read the file and split columns into two lists
        ///
        /// Read in the file and parse the data line by line
        /// splitting the line by a space and converting the values to integers
        /// and appending them to listA and listB
        /// </summary>
        /// <param name="inputFilePath">Path to the input file</param>
        /// <returns>List of two lists containing the values from the input file</returns>
        /// <exception cref="Exception">Thrown when the file cannot be read</exception>
        public static List<List<int>> parseInputFile(String inputFilePath)
        {
            //Create a list of lists to hold the input data
            Console.WriteLine("Parsing input file: " + inputFilePath);
            List<List<int>> metaList = new List<List<int>>();
            try
            {
                //Open a stream reader to read the file
                using (StreamReader sr = new StreamReader(inputFilePath))
                {
                    //Read the file line by line
                    string line;
                    while ((line = sr.ReadLine()) != null)
                    {
                        //Split the line by spaces and create a list of integers to hold the values
                        string[] split = line.Split(new char[0], StringSplitOptions.RemoveEmptyEntries);
                        List<int> intList = new List<int>();
                        foreach (string s in split)
                        {
                            //Parse the string to an integer and add it to the list
                            intList.Add(Int32.Parse(s));
                        }
                        //Add the list of integers to the meta list
                        metaList.Add(intList);
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("The file could not be read:");
                Console.WriteLine($"{e} : {e.Message}");
            }
            return metaList;
        }


        /// <summary>
        /// Check if the trend is continuing
        /// </summary>
        /// <param name="isIncreasing">Boolean representing what the current trend is</param>
        /// <param name="current">Current element in trend</param>
        /// <param name="next">Next element in trend</param>
        /// <returns></returns>
        public static bool isContinuingTrend(isIncreasing, int current, int next)
        {
            if(isIncreasing)
            {
                return current < next;
            }
            else
            {
                return next > current;
            }
        }

        /// <summary>
        /// Check if the difference between the a and b element is within a range of 
        /// </summary>
        /// <param name="a"></param>
        /// <param name="b"></param>
        /// <param name="min"></param>
        /// <param name="max"></param>
        /// <returns>Returns true if the difference between a and be is in the range of min and max</returns>
        public static bool isWithinRange(int a, int b, int min, int max)
        {
            int diff = Math.Abs(a - b);
            return min <= diff && diff <= max;
        }

        /// <summary>
        /// Check if the order of the ints is safe or unsafe
        ///
        /// Check if the order of the ints is safe or unsafe according to the following safety rules:
        /// 1. Ther order of the intes must be only increasing or decreasing
        /// 2. Any two adjacent ints must differ by at least 1 and at most 3
        ///
        /// </summary>
        /// <param name="list">List of integers</param>
        /// <returns>True if the list is safe, false otherwise</returns>
        public static bool listIsSafe(List<int> list)
        {
            //Check if the list is empty or has two elements that are the same
            if list.Count > 1 && (list[0] == list[1])
            {
                return false;
            }

            //Check if the list is increasing or decreasing
            bool isIncreasing = list[0] < list[1];

            for (int i = 1; i < list.Count - 1; i++)
            {
                //Check if the list is still increasing or decreasing
                if (!isContinuingTrend(isIncreasing, list[i-1], list[i]))
                {
                    return false;
                }

                //Check if the difference between the elements is within the range of 1 and 3
                if (!isWithinRange(list[i-1], list[i], 1, 3))
                {
                    return false;
                }
            }

            //If all the checks pass, the list is safe
            return true;
        }

        public static void Main(String[] args)
        {
            if(args.Length == 0 || args.Length == 1)
            {
                Console.WriteLine("Please provide an input file with -i argument");
                return;
            }

            if(args[1].Equals("-i"))
            {
                Console.WriteLine("Input file is: " + args[2]);
            }
            else
            {
                Console.WriteLine("Please provide an input file with -i argument");
            }

            //Parse the input file
            List<List<int>> metaList = parseInputFile(args[1]);

            //Initializse the safe count and lists
            int safeCount = 0;
            List<List<int>> safeList = new List<List<int>>();
            List<List<int>> unsafeList = new List<List<int>>();

            //Iterate over the lists and check if they are safe or unsafe
            foreach(List<int> list in metaList)
            {
                //Check if the list is safe
                bool isSafe = listIsSafe(list);
                if(isSafe(list))
                {
                    //Increment the safe count and add the list to the safe list
                    safeCount++;
                    safeList.Add(list);
                }
                else
                {
                    //Add the list to the unsafe list
                    unsafeList.Add(list);
                }
            }
            //Print the results
            Console.WriteLine($"Safe count: {safeCount}");

            // Problem Dampener i.e. part 2
            int dampenedSafeCount = safeCount;
            foreach(List<int> list in unsafeList)
            {
                //Iterate over the list and remove each element one by one
                for(int i = 0; i < list.Count; i++)
                {
                    //Create a temporary list and remove the element at index i
                    List<int> tempList = new List<int>(list);
                    tempList.RemoveAt(i);
                    //Check if the list is safe
                    if(listIsSafe(tempList))
                    {
                        //If the list is safe, increment the dampened safe count
                        // break out of the loop for the current list
                        // because we already showed that it can be made safe
                        dampenedSafeCount++;
                        break;
                    }
                }
            }
        }
    }
}