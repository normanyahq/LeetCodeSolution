class Solution {
public:
    int maxProfit(int k, vector<int>& old_prices) {
        if (old_prices.empty())
            return 0;
            
        /* Compress the prices, merge continously increasing and decreasing intervals */
        vector<int> prices;
        bool first_element = true;
        int i=1;
        while (i < old_prices.size()) {
            while (i < old_prices.size() && old_prices[i] <= old_prices[i-1])
                i++;
            if (i >= old_prices.size())
                break;
            auto t1 = old_prices[i-1];
            while (i < old_prices.size() && old_prices[i] >= old_prices[i-1])
                i++;
            prices.push_back(t1);
            prices.push_back(old_prices[i-1]);
        }
        /* Compress the prices, merge continously increasing and decreasing intervals */

        
        /** Optimization for Special Case **/
        // if k is larger than the largest possible number of transections,
        // simply sum up all the profits in the intervals.
        if (prices.size() < 2)
            return 0;
        if (k >= prices.size() / 2) {
            int result = 0;
            for (int i=(prices[0] > prices[1]) + 1; i<prices.size(); i+=2)
                result += (prices[i] - prices[i-1]) * (prices[i] > prices[i-1] ? 1 : -1);
            return result;
        }
        /** Optimization for Special Case **/
        
        vector<int> f;
        f.push_back(0);
        f.push_back(INT_MIN);
        int best = 0;
        
        /** Typical k-state DP for stock problems **/
        // one optimization is, if we haven't updated state f[i] yet, then we don't 
        // need to loop through f[i+1], f[i+2], ...
        for (int i=0; i<prices.size(); i++) {
            for (int j=f.size()-1; j>0; j--) {
                auto t = f[j];
                if (j % 2)
                    f[j] = std::max(f[j-1] - prices[i], f[j]);
                else {
                    f[j] = std::max(f[j-1] + prices[i], f[j]);
                    best = std::max(f[j], best);
                }
                if (j == f.size() - 1 && t != f[j] && (f.size()-1) / 2 < k) // if f[j] updated
                    f.push_back((j+1) % 2 ? INT_MIN : 0);
            }
        }
        /** Typical k-state DP for stock problems **/

        return best;
    }
};
