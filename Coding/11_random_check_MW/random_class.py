class CheckNonPrimitive:
    def __init__(self, df, seeds):
        self.df = df.copy()
        self.buckets = dict()
        self.seeds = seeds

    def get_stats(self):
        print("Rows: ", self.df.shape[0])
        print("Columns: ", self.df.shape[1])
        print("Column Names: ", self.df.columns)

    def get_shape(self):
         return self.df.shape

    def add_index(self):
        self.df["Index"] = range(1, self.df.shape[0] + 1)

    def init_buckets(self):
        lis = list(range(1, self.df.shape[0] + 1))

        def backtrack(subs, visited):
            if len(subs) == len(lis):
                self.buckets[tuple(subs)] = []
                return

            for i in range(len(lis)):
                if visited[i]:
                    continue

                subs.append(lis[i])
                visited[i] = 1

                backtrack(subs, visited)

                visited[i] = 0
                subs.pop()

        backtrack([], [0] * len(lis))
