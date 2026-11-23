import java.util.Arrays;

/** Small sorting exercise, standard Java only. */
public class SelectionSort {
    public static void sort(int[] values) {
        for (int i = 0; i < values.length; i++) {
            int smallest = i;
            for (int j = i + 1; j < values.length; j++) {
                if (values[j] < values[smallest]) smallest = j;
            }
            int swap = values[i];
            values[i] = values[smallest];
            values[smallest] = swap;
        }
    }

    public static void main(String[] args) {
        int[] values = {5, 1, 4, 2, 3};
        sort(values);
        System.out.println(Arrays.toString(values));
    }
}
