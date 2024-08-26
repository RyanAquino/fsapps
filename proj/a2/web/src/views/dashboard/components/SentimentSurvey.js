import React, { useEffect, useState } from 'react';
import { useTheme } from '@mui/material/styles';
import DashboardCard from '../../../components/shared/DashboardCard';
import Chart from 'react-apexcharts';
import {sentimentSurvey} from '../../../api/utils';
import { useNavigate } from 'react-router-dom';

const SentimentSurvey = () => {
  const [tableData, setTableData] = useState([]);
  const navigate = useNavigate();
  const loginRoute = '/auth/login';

  useEffect(() => {
    const token = localStorage.getItem('token');

    if (!token) {
      navigate(loginRoute);
    }

    const fetchTableData = async () =>
      await sentimentSurvey(token).catch((err) => {
        console.log(err);
        if (err.response.status === 401) {
          navigate(loginRoute);
        }
      });

    fetchTableData().then((tableData) => {
      let data = [];

      for (const item of tableData) {
        data.push({
          record_date: item['record_date'],
          bullish: item['bullish'],
          neutral: item['neutral'],
          bearish: item['bearish'],
        });
      }

      setTableData(data);
    });
  }, []);

  const theme = useTheme();
  const primary = theme.palette.primary.main;
  const secondary = theme.palette.secondary.main;
  const tertiary = theme.palette.error.main;

  console.log()

  const optionscolumnchart = {
    chart: {
      height: 350,
      type: 'line',
      dropShadow: {
        enabled: true,
        color: '#000',
        top: 18,
        left: 7,
        blur: 10,
        opacity: 0.2,
      },
    },
    colors: [primary, secondary, tertiary],
    markers: {
      size: 0.5,
    },
    stroke: {
      curve: 'smooth',
    },
    grid: {
      borderColor: '#e7e7e7',
      row: {
        colors: ['#f3f3f3', 'transparent'],
        opacity: 0.5,
      },
    },
    xaxis: {
      categories: tableData.map((i) => i['record_date']),
      type: 'datetime',
      title: {
        text: 'Day',
      },
    },
    yaxis: {
      title: {
        text: 'Percentage',
      },
      type: "string",
      min: 0,
      max: Math.max(
          ...tableData.map((i) => i['bearish'] ? i["bearish"] : 0),
          ...tableData.map((i) => i['neutral'] ? i['neutral'] : 0),
          ...tableData.map((i) => i['bullish'] ? i['bullish'] : 0),
      ),
    },
    legend: {
      position: 'bottom',
    },
  };

  const seriescolumnchart = [
    {
      name: 'Bullish',
      data: tableData.map((i) => `${i['bullish']}%` ? i['bullish'] : 0),
    },
    {
      name: 'Neutral',
      data: tableData.map((i) => i['neutral'] ? i['neutral'] : 0),
    },
    {
      name: 'Bearish',
      data: tableData.map((i) => i['bearish'] ?  i['bearish'] : 0),
    },
  ];

  return (
    <DashboardCard title="Sentiment Survey">
      <Chart options={optionscolumnchart} series={seriescolumnchart} type="line" height="270px" />
    </DashboardCard>
  );
};

export default SentimentSurvey;
