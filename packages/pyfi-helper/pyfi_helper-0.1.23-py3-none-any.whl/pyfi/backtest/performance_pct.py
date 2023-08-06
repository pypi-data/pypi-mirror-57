
def asset_with_weight(pct_df, weight_df, freq="M"):
    """
    传入资产价格dataframe和权重dataframe，构建净值曲线
    """
    if freq == "M":
        pct_df = pct_df.resample("M").last().ffill()
        weight_df = weight_df.resample("M").last().ffill()
    elif freq == "D":
        pct_df = pct_df.resample("D").last().ffill()
        weight_df = weight_df.resample("D").last().ffill()
    else:
        raise Exception("频率设置有问题！")
    return (1+pct_df*weight_df.sum(axis=1)).cumprod()



