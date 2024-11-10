// See https://aka.ms/new-console-template for more information

using System.Runtime.CompilerServices;

public class Program
{
    private static void Main()
    {   
        Title();
        years();    
        }

    private static void Title()
    {
        Console.WriteLine(
            @"
               __  __       _   _       _____                          _
              |  \/  | __ _| |_| |__   |  ___|__  _ __ _ __ ___  _   _| | __ _ ___
              | |\/| |/ _` | __| '_ \  | |_ / _ \| '__| '_ ` _ \| | | | |/ _` / __|
              | |  | | (_| | |_| | | | |  _| (_) | |  | | | | | | |_| | | (_| \__ \
              |_|  |_|\__,_|\__|_| |_| |_|  \___/|_|  |_| |_| |_|\__,_|_|\__,_|___/
            ");

        Console.WriteLine(
            @"
                ____            _   _       _     _     _
               | __ ) _   _    | \ | | __ _| |__ (_) __| | __ _
               |  _ \| | | |   |  \| |/ _` | '_ \| |/ _` |/ _` |
               | |_) | |_| |_  | |\  | (_| | | | | | (_| | (_| |
               |____/ \__, (_) |_| \_|\__,_|_| |_|_|\__,_|\__,_|
                      |___/
            ");
    }

    private static void yearselector(){
        Console.WriteLine("[1] 1°Year");
        Console.WriteLine("[2] 2°Year");
        Console.WriteLine("[3] 3°Year");
        Console.WriteLine("[0] Exit"); 
    }
    

    private static void firstyear_semesterselector(){
        Console.WriteLine("\n[1] 1°Semester");
        Console.WriteLine("[2] 2°Semester");
        Console.WriteLine("[0] Back\n");
    }

    private static void final_firstyear_semesterselector(){
        firstyear_semesterselector();

        Console.WriteLine("Enter the semester: ");
        string semester = Console.ReadLine() ?? string.Empty; 
        //semester = int(semester)

        if (semester == "1"){
            firstsemester_partialselector(); 
        }else if (semester == "2"){
            secondsemester_partialselector();
        } else if (semester == "0"){
            Console.WriteLine("\nReturning to the main menu...\n");
            Thread.Sleep(2);
            years();
        }else {
            Console.WriteLine("Invalid semester!");
            }
    }
    

    private static void secondyear_semesterselector(){
        Console.WriteLine("\n[3] 3°Semester");
        Console.WriteLine("[4] 4°Semester");
        Console.WriteLine("[0] Back\n");
    }

    private static void final_secondyear_semesterselector(){
        secondyear_semesterselector();

        Console.WriteLine("Enter the semester: ");
        string semester = Console.ReadLine() ?? string.Empty; 
        //semester = int(semester)

    if (semester == "3"){
        thirdsemester_partialselector();
        } else if (semester == "4"){
            fourthsemester_partialselector();
        } else if (semester == "0"){
            Console.WriteLine("\nReturning to the main menu...\n");
            Thread.Sleep(2);
            years();
        } else{
            Console.WriteLine("Invalid semester!");
        }
    }

    private static void thirdyear_semesterselector(){
        Console.WriteLine("\n[5] 5°Semester");
        Console.WriteLine("[6] 6°Semester");
        Console.WriteLine("[0] Back\n");
    }
        

    private static void final_thirdyear_semesterselector(){
        thirdyear_semesterselector();

        Console.WriteLine("Enter the semester: ");
        string semester = Console.ReadLine() ?? string.Empty; 
        //semester = int(semester)

        if (semester == "5"){
            fifthsemester_partialselector();
        }else if (semester == "6"){
            sixthsemester_partialselector();
        } else if (semester == "0"){
            Console.WriteLine("\nReturning to the main menu...\n");
            Thread.Sleep(2);
            years();
        }else{
            Console.WriteLine("Invalid semester!");
        }
    }

    private static void partialselector(){
        Console.WriteLine("\n[1] Partial 1");
        Console.WriteLine("[2] Partial 2");
        Console.WriteLine("[3] Partial 3");
        Console.WriteLine("[4] Partial 4");
        Console.WriteLine("[5] Institutional Exam");
    }

    private static void firstsemester_partialselector(){
        partialselector();
        
        Console.WriteLine("\nEnter the partial: ");
        string firstsemesterpartials = Console.ReadLine() ?? string.Empty;
        //firstsemesterpartials = int(firstsemesterpartials)

        if (firstsemesterpartials == "1"){
            final_Firstyear_Firstsemester_Firstpartial_themeselector();
        } else if (firstsemesterpartials == "2"){
            Console.WriteLine("Partial 2");
        }else if (firstsemesterpartials == "3"){
            Console.WriteLine("Partial 3");
        }else if (firstsemesterpartials == "4"){
            Console.WriteLine("Partial 4");
        }else if (firstsemesterpartials == "5"){
            Console.WriteLine("Institutional Exam");
        }else if (firstsemesterpartials == "0"){
            Thread.Sleep(2);
            final_firstyear_semesterselector();
        }else{
            Console.WriteLine("Invalid input.");
        }
    }
private static void secondsemester_partialselector(){
        partialselector();

        Console.WriteLine("\nEnter the partial: ");
        string secondsemesterpartials = Console.ReadLine() ?? string.Empty;
        //secondsemesterpartials = int(secondsemesterpartials)
        //int secondsemesterpartia_int = int.Parse(secondsemesterpartials);

        if (secondsemesterpartials == "1"){
            Console.WriteLine("Partial 1");
        }else if (secondsemesterpartials == "2"){
            Console.WriteLine("Partial 2");
        }else if (secondsemesterpartials == "3"){
            Console.WriteLine("Partial 3");
        }else if (secondsemesterpartials == "4"){
            Console.WriteLine("Partial 4");
        }else if (secondsemesterpartials == "5"){
            Console.WriteLine("Institutional Exam");
        }else if (secondsemesterpartials == "0"){ 
            Thread.Sleep(2);
            final_firstyear_semesterselector();
        }else{
            Console.WriteLine("Invalid input.");
        }
    }

    private static void thirdsemester_partialselector(){
        partialselector();

        Console.WriteLine("\nEnter the partial: ");
        string thirdsemesterpartials = Console.ReadLine() ?? string.Empty;
        //thirdsemesterpartials = int(thirdsemesterpartials)

        if (thirdsemesterpartials == "1"){
        final_Secondyear_Thirdsemester_Firstpartial_themeselector();
        }else if (thirdsemesterpartials == "2"){
        final_Secondyear_Thirdsemester_Secondpartial_themeselector();
        }else if (thirdsemesterpartials == "3"){
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector();
        }else if (thirdsemesterpartials == "4"){
        Console.WriteLine("Partial 4");
        }else if (thirdsemesterpartials == "5"){
        Console.WriteLine("Institutional Exam");
        }else if (thirdsemesterpartials == "0"){
        Thread.Sleep(2);
        final_secondyear_semesterselector();
        }else{
        Console.WriteLine("Invalid input.");
        }
    }
        private static void fourthsemester_partialselector(){
        partialselector();
        Console.WriteLine("\nEnter the partial: ");
        string fourthsemesterpartials = Console.ReadLine() ?? string.Empty;
        //fourthsemesterpartials = int(fourthsemesterpartials)

        if (fourthsemesterpartials == "1"){
        Console.WriteLine("Partial 1");
        }else if (fourthsemesterpartials == "2"){
        Console.WriteLine("Partial 2");
        }else if (fourthsemesterpartials == "3"){
        Console.WriteLine("Partial 3");
        }else if (fourthsemesterpartials == "4"){
        Console.WriteLine("Partial 4");
        }else if (fourthsemesterpartials == "5"){
        Console.WriteLine("Institutional Exam");
        }else if (fourthsemesterpartials == "0"){
        Thread.Sleep(2);
        final_secondyear_semesterselector();
        }else{
        Console.WriteLine("Invalid input.");
        }
    }
        
    
    private static void fifthsemester_partialselector(){
    partialselector();
    Console.WriteLine("\nEnter the partial: ");

    string fifthsemesterpartials = Console.ReadLine() ?? string.Empty;
    //fifthsemesterpartials = int(fifthsemesterpartials)

    if (fifthsemesterpartials == "1"){
        Console.WriteLine("Partial 1");
    }else if (fifthsemesterpartials == "2"){
        Console.WriteLine("Partial 2");
    }else if (fifthsemesterpartials == "3"){
        Console.WriteLine("Partial 3");
    }else if (fifthsemesterpartials == "4"){
        Console.WriteLine("Partial 4");
    }else if (fifthsemesterpartials == "5"){
        Console.WriteLine("Institutional Exam");
    }else if (fifthsemesterpartials == "0"){
        Thread.Sleep(2);
        final_thirdyear_semesterselector();
    }else{
        Console.WriteLine("Invalid input.");
        }
    }

    private static void sixthsemester_partialselector(){
    partialselector();

    Console.WriteLine("\nEnter the partial: ");
    string sixthsemesterpartials = Console.ReadLine() ?? string.Empty;
    //sixthsemesterpartials = int(sixthsemesterpartials)

    if (sixthsemesterpartials == "1"){
        Console.WriteLine("Partial 1");
    }else if (sixthsemesterpartials == "2"){
        Console.WriteLine("Partial 2");
    }else if (sixthsemesterpartials == "3"){
        Console.WriteLine("Partial 3");
    }else if (sixthsemesterpartials == "5"){
        Console.WriteLine("Institutional Exam");
    }else if (sixthsemesterpartials == "0"){ 
        Thread.Sleep(2);
        final_thirdyear_semesterselector();
    }else{
        Console.WriteLine("Invalid input.");
        }
    }   
private static void years(){
    yearselector();
    Console.WriteLine("\nEnter your year of study: ");;
    string year = Console.ReadLine() ?? string.Empty;
    //year = int(year)

    if (year == "1"){
        final_firstyear_semesterselector();

    }else if (year == "2"){
        final_secondyear_semesterselector();
    
    }else if (year == "3"){
        final_thirdyear_semesterselector();
    
    }else if (year == "0"){
        Console.WriteLine("\nExiting...");
        Thread.Sleep(2);
        Console.WriteLine("Thank for using it.");
        Environment.Exit(0);
    }else{
        Console.WriteLine("Invalid input.");
        }
    }

    private static void Secondyear_Thirdsemester_Firstpartial_themeselector(){
    Console.WriteLine("\n[1] Distance between two points");
    Console.WriteLine("[2] Area");
    Console.WriteLine("[3] Ratio of a line segment");
    Console.WriteLine("[4] Coordinates of ratio in a line segment");
    Console.WriteLine("[5] Midpoint of a line segment");
    Console.WriteLine("[0] Back\n");
    }
    private static void final_Secondyear_Thirdsemester_Firstpartial_themeselector(){
    Secondyear_Thirdsemester_Firstpartial_themeselector();

    Console.WriteLine("\nEnter the theme: ");

    string thirdsemesterFirstPartialTheme = Console.ReadLine() ?? string.Empty;
    //thirdsemesterFirstPartialTheme = int(thirdsemesterFirstPartialTheme);

    if (thirdsemesterFirstPartialTheme == "1"){
        MathFormulas.distance_between_two_points();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Firstpartial_themeselector();
    }else if( thirdsemesterFirstPartialTheme == "2"){
        //mathF.Area();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Firstpartial_themeselector();
    }else if (thirdsemesterFirstPartialTheme == "3"){
        //mathF.ratio_of_a_line_segment();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Firstpartial_themeselector();
    }else if (thirdsemesterFirstPartialTheme == "4"){
        //mathF.coordinates_of_ratio();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Firstpartial_themeselector();
    }else if (thirdsemesterFirstPartialTheme == "5"){
        //mathF.midpoint_of_a_line_segment();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Firstpartial_themeselector();
    }else if (thirdsemesterFirstPartialTheme == "0"){
        Thread.Sleep(2);
        thirdsemester_partialselector();
    }else{
        Console.WriteLine("Invalid input.");
        }
    }

    private static void Firstyear_Firstsemester_Firstpartial_themeselector(){
    //Sets may be added later
    Console.WriteLine("[0] Back\n");
    }

    private static void final_Firstyear_Firstsemester_Firstpartial_themeselector(){
    Firstyear_Firstsemester_Firstpartial_themeselector();

    Console.WriteLine("\nEnter the theme: ");
    string firstsemesterFirstPartialTheme = Console.ReadLine() ?? string.Empty;
    //firstsemesterFirstPartialTheme = int(firstsemesterFirstPartialTheme)

    if (firstsemesterFirstPartialTheme == "0"){ //Back
        Thread.Sleep(2);
        firstsemester_partialselector();
    }else{
        Console.WriteLine("Invalid input.");
        }
    }

    private static void Secondyear_Thirdsemester_Secondpartial_themeselector(){
    Console.WriteLine("\n[1] Slope");
    Console.WriteLine("[2] Get Slope from an Angle");
    Console.WriteLine("[3] Angle between lines");
    Console.WriteLine("[0] Back\n");
    }

private static void final_Secondyear_Thirdsemester_Secondpartial_themeselector(){
    Secondyear_Thirdsemester_Secondpartial_themeselector();

    Console.WriteLine("\nEnter the theme: ");
    string thirdsemesterSecondPartialTheme = Console.ReadLine() ?? string.Empty;
    //thirdsemesterSecondPartialTheme = int(thirdsemesterSecondPartialTheme)

    if (thirdsemesterSecondPartialTheme == "1"){
        //mathF.slope();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Secondpartial_themeselector();
    }else if (thirdsemesterSecondPartialTheme == "2"){
        //mathF.slope_from_angle();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Secondpartial_themeselector();
    }else if (thirdsemesterSecondPartialTheme == "3"){
        //mathF.angle_between_lines();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Secondpartial_themeselector();
    }else if (thirdsemesterSecondPartialTheme == "0"){ //Back
        Thread.Sleep(2);
        thirdsemester_partialselector();
    }else{
        Console.WriteLine("Invalid input.");
        }
    }

    private static void Secondyear_Thirdsemester_Thirdpartial_themeselector(){
    Console.WriteLine("\n[1] Point-Slope equation of a line");
    Console.WriteLine("[2] Equation of a line that passes through 2 points");
    Console.WriteLine("[3] Symmetric equation to ordinary");
    Console.WriteLine("[4] General to Symmetric equation");
    Console.WriteLine("[5] Points to General circumference equation");
    Console.WriteLine("[6] General circumference equation to Points" );
    Console.WriteLine("[0] Back\n");
    }
private static void final_Secondyear_Thirdsemester_Thirdpartial_themeselector(){
    Secondyear_Thirdsemester_Thirdpartial_themeselector();

    Console.WriteLine("\nEnter the theme: ");
    string thirdsemesterThirdPartialTheme = Console.ReadLine() ?? string.Empty;
    //thirdsemesterThirdPartialTheme = int(thirdsemesterThirdPartialTheme)

    if (thirdsemesterThirdPartialTheme == "1"){
        //mathF.point_slope_equaton_of_a_line();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector();
    }else if (thirdsemesterThirdPartialTheme == "2"){
        //mathF.Equation_of_a_line_that_passes_through_2_points();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector();
    }else if (thirdsemesterThirdPartialTheme == "3"){
        //mathF.Symmetric_equation_to_ordinary();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector();
    }else if (thirdsemesterThirdPartialTheme == "4"){
        //mathF.general_to_symmetric_equations();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector();
    }else if (thirdsemesterThirdPartialTheme == "5"){
        //mathF.points_to_general_circumference_equation();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector();
    }else if (thirdsemesterThirdPartialTheme == "6"){
        //mathF.from_general_to_points();
        Thread.Sleep(5);
        final_Secondyear_Thirdsemester_Thirdpartial_themeselector();
    }else if (thirdsemesterThirdPartialTheme == "0"){ //Back
        Thread.Sleep(2);
        thirdsemester_partialselector();
    }else{
        Console.WriteLine("Invalid input.");
        }
    }
}

public class MathFormulas{
    public static void distance_between_two_points(){

    Console.WriteLine("\nEnter the first coordinate (x, y): ");
    string input = Console.ReadLine() ?? string.Empty;
    string[] coordinates = input.Split(" ");

    Console.WriteLine("\nEnter the Second coordinate (x, y): ");
    string input2 = Console.ReadLine() ?? string.Empty;
    string[] coordinates2 = input2.Split(" ");
    
    if (coordinates.Length == 2 && coordinates2.Length == 2){
        string x1_str = coordinates[0]; 
        string y1_str = coordinates[1];

        string x2_str = coordinates2[0];
        string y2_str = coordinates2[1];

        double x1 = double.Parse(x1_str);
        double y1 = double.Parse(y1_str);
        
        double x2 = double.Parse(x2_str);
        double y2 = double.Parse(y2_str);

        double distance = Math.Sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)));

        //Console.WriteLine("\nThe distance between the two points is: "+distance+"u" );
        Console.WriteLine($"\nThe distance between the two points is: {distance}u" );
    } else {
        Console.WriteLine("Invalid input!!!");
    }
    }
}

