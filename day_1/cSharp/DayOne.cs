using System;

public class Program {

    /// <summary>
    /// Parses the input file.
    /// </summary>
    public static List<List<int>> parseInputFile(String inputFilePath) {
        Console.WriteLine("Parsing input file: " + inputFilePath);
        List<List<int>> lists = new List<List<int>>();
        List<int> listA = new List<int>();
        List<int> listB = new List<int>();
        try {
            using (StreamReader sr = new StreamReader(inputFilePath)) {
                string line;
                while ((line = sr.ReadLine()) != null) {
                    string[] split = line.Split(new char[0], StringSplitOptions.RemoveEmptyEntries);
                    listA.Add(Int32.Parse(split[0]));
                    listB.Add(Int32.Parse(split[1]));
                }
            }
        } catch (Exception e) {
            Console.WriteLine("The file could not be read:");
            Console.WriteLine($"{e} : {e.Message}");
        }
        lists.Add(listA);
        lists.Add(listB);
        return lists;
    }

    /// <summary>
    /// Builds a count map of the elements in the list
    /// </summary>
    /// <param name="list">List to create count map of</param>
    /// <returns></returns>
    public static Dictionary<int, int> buildCountMap(List<int> list) {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        foreach(int num in list) {
            if(dict.ContainsKey(num)) {
                dict[num] += 1;
            } else {
                dict[num] = 1;
            }
        }
        return dict;
    }

    /// <summary>
    /// Finds the sum of the elements in the list multiplied by their count in the countMap
    /// </summary>
    /// <param name="list">List to get the adjusted sum for</param>
    /// <param name="countMap">A map countaining all the counts of elements found in the parallel list</param>
    /// <returns></returns>
    public static int findSum(List<int> list, Dictionary<int, int> countMap){
        int sum = 0;
        foreach(int element in list) {
            if(countMap.ContainsKey(element)) {
                sum += element * countMap[element];
            }
        }
        return sum;
    }

    /// <summary>
    /// Main method
    /// </summary>
    /// <param name="args">Commandline args (duh)</param>
    public static void Main(String[] args) {
        if(args.Length == 0 || args.Length == 1) {
            Console.WriteLine("Please provide an input file with -i argument");
            return;
        }

        if(args[1].Equals("-i")) {
            Console.WriteLine("Input file is: " + args[2]);
        } else {
            Console.WriteLine("Please provide an input file with -i argument");
        }

        List<List<int>> lists = parseInputFile(args[1]);
        List<int> listA = lists[0];
        List<int> listB = lists[1];

        listA.Sort();
        listB.Sort();

        int totalDistance = 0;

        for(int i = 0; i < listA.Count; i++) {
            totalDistance += Math.Abs(listA[i] - listB[i]);
        }
        Console.WriteLine($"Total distance between the two lists: {totalDistance}");

        Dictionary<int, int> countMap = buildCountMap(listB);
        int sum = findSum(listA, countMap);

        Console.WriteLine($"Sum of the elements in list A multiplied by their count in list B: {sum}");
    }

}