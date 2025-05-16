import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int testCount = 20;
        int initialSize = 1000;

        String dataDir = "data";
        File dir = new File(dataDir);
        if (!dir.exists()) {
            dir.mkdirs();
        }
        String outputPath = dataDir + "/execution_times.csv";

        System.out.println("Working directory: " + System.getProperty("user.dir"));
        System.out.println("Output CSV path: " + new File(outputPath).getAbsolutePath());

        try (FileWriter writer = new FileWriter(outputPath)) {
            writer.append("Algorithm;Size;Time(ms)\n");

            for (int i = 1; i <= testCount; i++) {
                int size = initialSize * i;
                int[] baseArray = generateRandomArray(size);

                benchmarkSort("BubbleSort", baseArray, writer);
                benchmarkSort("MergeSort", baseArray, writer);
                benchmarkSort("QuickSort", baseArray, writer);
            }

            System.out.println("CSV saved to: " + outputPath);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void benchmarkSort(String sortName, int[] originalArray, FileWriter writer) throws IOException {
        int[] array = Arrays.copyOf(originalArray, originalArray.length);
        long start = System.nanoTime();

        switch (sortName) {
            case "BubbleSort":
                BubbleSort.sort(array);
                break;
            case "MergeSort":
                MergeSort.sort(array);
                break;
            case "QuickSort":
                QuickSort.sort(array, 0, array.length - 1);
                break;
        }

        long end = System.nanoTime();
        long durationMs = (end - start) / 1_000_000;

        writer.append(String.format("%s;%d;%d\n", sortName, array.length, durationMs));
    }

    public static int[] generateRandomArray(int size) {
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = (int) (Math.random() * 100000);
        }
        return array;
    }
}