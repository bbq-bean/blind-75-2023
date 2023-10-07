class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if log == "../":
                if not stack:
                    continue
                else:
                    stack.pop()

            elif log == "./":
                continue

            else:
                stack.append(log.split("/")[0])

        return len(stack)
