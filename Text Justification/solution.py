class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        left = 0
        while left < len(words):
            cur_width = len(words[left])
            right = left + 1
            while right < len(words) and cur_width + len(words[right]) + 1 <= maxWidth:
                cur_width += 1 + len(words[right])
                right += 1
            right -= 1
            if left == right:
                result.append(words[left] + ' ' * (maxWidth - cur_width))
                left = right + 1
                continue
            space_count = [1] * (right - left)
            space_left = maxWidth - cur_width
            for i in range(right-left):
                if i < space_left % (right - left):
                    space_count[i] += 1
                space_count[i] += space_left / (right - left)
            line = words[left]
            for i in range(right-left):
                line += " " * space_count[i] + words[left + i + 1]
            if right == len(words) - 1:
                line = " ".join(line.split())
                line += " " * (maxWidth - len(line))
            result.append(line)
            left = right + 1
        return result
