details = {
  "kmeans":[
    {
      "name":"k",
      "display":"聚类数目",
      "type":"number",
      "default":"2",
    },
    {
      "name":"maxIterations",
      "display":"最大迭代次数",
      "type":"number",
      "default":"20"
    }
  ],
  "fpgrowth":[
    {
      "name":"minSupport",
      "display":"最小支持度",
      "type":"number",
      "default":"0.3",
    },
  ],
  "logistic-regression":[
    {
      "name":"iterations",
      "display":"迭代次数",
      "type":"number",
      "default":"100",
    },
    {
      "name":"label",
      "display":"标签列",
      "type":"number",
      "default":"0"
    },
    {
      "name":"numClasses",
      "display":"标签类别数",
      "type":"number",
      "default":"2",
    }
  ],
  "knn":[
    {
      "name":"method",
      "display":"方法",
      "type":"list",
      "default":"classify",
      "list":[
        "classify",
        "regress"
      ]
    },
    {
      "name":"label_columns",
      "display":"标签列",
      "type":"text",
      "default":"label"
    }
  ],
  "naive-bayes":[
    {
      "name":"label_columns",
      "display":"标签列",
      "type":"text",
      "default":"label"
    }
  ],
  "decision-tree":[
    {
      "name":"method",
      "display":"方法",
      "type":"list",
      "default":"classify",
      "list":[
        "classify",
        "regress"
      ]
    },
    {
      "name":"label_columns",
      "display":"标签列",
      "type":"text",
      "default":"label"
    }
  ],
  "sql-instream":[
    {
      "name":"read_number",
      "display":"读入数量",
      "type":"number",
      "default":"0"
    },
    {
      "name":"database-type",
      "display":"数据库类型",
      "type":"list",
      "default":"MySQL",
      "list":[
        "MySQL",
        "sqlite",
        "oracle",
        "SQLServer",
        "PostgreSQL"
      ]
    },
    {
      "name":"address",
      "display":"地址",
      "type":"text",
      "default":"localhost"
    },
    {
      "name":"port",
      "display":"端口",
      "type":"text",
      "default":"3306"
    },
    {
      "name":"user",
      "display":"账号",
      "type":"text",
      "default":"root"
    },
    {
      "name":"password",
      "display":"密码",
      "type":"password",
      "default":"123"
    },
    {
      "name":"database-name",
      "display":"数据库名",
      "type":"text",
      "default":""
    },
    {
      "name":"command",
      "display":"SQL查询语句",
      "type":"richtext",
      "default":"SELECT *\nFROM tableA"
    }
  ],
  "model-instream":[
    {
      "name":"path",
      "display":"文件名",
      "type":"text",
      "default":""
    },
    {
      "name":"type",
      "display":"模型类型",
      "type":"list",
      "default":"kmeans",
      "list": Object.keys(type_id['algorithm']),
    },
  ],
  "data-outstream":[
    {
      "name":"path",
      "display":"文件名",
      "type":"text",
      "default":""
    }
  ],
  "data-instream":[
    {
      "name":"path",
      "display":"文件名",
      "type":"text",
      "default":""
    },
    {
      "name":"type",
      "display":"类型",
      "type":"list",
      "default":"file",
      "list":[
        "file",
        "folder",
      ]
    },
    {
      "name":"separator",
      "display":"拆分符号",
      "type":"text",
      "default":",",
    },
    {
      "name":"charset",
      "display":"字符编码",
      "type":"list",
      "default":"utf-8",
      "list":[
          "utf-8",
          "gbk",
      ],
    },
  ],
  "map":[
    {
      "name":"lambda",
      "display":"lambda表达式",
      "type":"text",
      "default":"lambda row: row",
    },
  ],
  "filter":[
    {
      "name":"lambda",
      "display":"lambda表达式",
      "type":"text",
      "default":"lambda row: row[0] == 0",
    }
  ],
  "sample":[
    {
      "name":"fraction",
      "display":"采样百分比(0-100)%",
      "type":"number",
      "default":"10",
    }
  ],
  "sql-outstream":[
    {
      "name":"database-type",
      "display":"数据库类型",
      "type":"list",
      "default":"MySQL",
      "list":[
        "MySQL",
        "sqlite",
        "oracle",
        "SQLServer",
        "PostgreSQL"
      ]
    },
    {
      "name":"address",
      "display":"地址",
      "type":"text",
      "default":"localhost"
    },
    {
      "name":"port",
      "display":"端口",
      "type":"text",
      "default":"3306"
    },
    {
      "name":"user",
      "display":"账号",
      "type":"text",
      "default":"root"
    },
    {
      "name":"password",
      "display":"密码",
      "type":"password",
      "default":"root"
    },
    {
      "name":"database-name",
      "display":"数据库名",
      "type":"text",
      "default":""
    },
    {
      "name":"table-name",
      "display":"表名",
      "type":"text",
      "default":""
    },
    {
      "name":"if_exists",
      "display":"冲突解决方式",
      "type":"list",
      "default":"fail",
      "list":[
        "replace",
        "append",
        "fail"
      ]
    }
  ],
  "model-outstream":[
    {
      "name":"path",
      "display":"文件名",
      "type":"text",
      "default":""
    }
  ],
  "sort":[
    {
      "name":"columns",
      "display":"列",
      "type":"number",
      "default":"0"
    },
    {
      "name":"ascending",
      "display":"升序",
      "type":"list",
      "default":"True",
      "list":[
        "True",
        "False"
      ]
    },
    // {
    //   "name":"na_position",
    //   "display":"Nan所在位置",
    //   "type":"list",
    //   "default":"last",
    //   "list":[
    //     "first",
    //     "last"
    //   ]
    // }
  ],
  "random":[],
  "cache":[],
  "distinct-col":[
    {
      "name":"columns",
      "display":"列",
      "type":"number",
      "default":"0"
    },
  ],
  "distinct-row":[
  ],
  // "sql-execute":[
  //   {
  //     "name":"sql_command",
  //     "display":"SQL语句,用{this}指代该表",
  //     "type":"richtext",
  //     "default":"SELECT * \nFROM {this}"
  //   }
  // ],
  "normalization":[
    {
      "name":"method",
      "display":"标准化方式",
      "type":"list",
      "default":"no",
      "list":[
        "no",
        "int",
        "float",
      ]
    },
    // {
    //   "name":"columns",
    //   "display":"列",
    //   "type":"number",
    //   "default":"0"
    // }
  ],
  "fillna":[
    {
      "name":"fill_type",
      "display":"填充方式",
      "type":"list",
      "default":"all",
      "list":[
        "all",
        "specific",
        "ffill"
      ]
    },
    {
      "name":"value",
      "display":"值(all,specific)",
      "type":"text",
      "default":"0"
    }
  ],
  "drop_duplicate":[
    {
      "name":"columns",
      "display":"过滤列名",
      "type":"text",
      "default":""
    },
    {
      "name":"keep",
      "display":"保留方式",
      "type":"list",
      "default":"first",
      "list":[
        "first",
        "last",
        "None"
      ]
    }
  ],
  "dropna":[
    {
      "name":"drop_type",
      "display":"类型",
      "type":"list",
      "default":"row",
      "list":[
        "row",
        "col",
        "all"
      ]
    }
  ],
  "predict":[
    {
      "name":"label_columns",
      "display":"非特征列名",
      "type":"text",
      "default":"label"
    },
    {
      "name":"predict_labels",
      "display":"预测结果列名",
      "type":"text",
      "default":"predict"
    },
    {
      "name":"store_origin",
      "display":"输出保留原数据",
      "type":"list",
      "default":"False",
      "list":[
        "True",
        "False"
      ]
    }
  ],
  "split-col":[
    {
      "name":"start",
      "display":"开始index（包含）",
      "type":"number",
      "default":"0",
    },
    {
      "name":"end",
      "display":"结束index（不包含）",
      "type":"number",
      "default":"1",
    },
  ],
  // "split-row":[
  //   {
  //     "name":"ratio",
  //     "display":"拆分比例(0-100%)",
  //     "type":"number",
  //     "default":"75"
  //   }
  // ],
  // "merge-row":[],
  // "merge-col":[
  //   {
  //     "name":"how",
  //     "display":"合并方式",
  //     "type":"list",
  //     "default":"concat",
  //     "list":[
  //       "concat",
  //       "inner",
  //       "left",
  //       "right",
  //       "outer"
  //     ]
  //   }
  // ]
};
