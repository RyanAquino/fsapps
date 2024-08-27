import React, { useState } from 'react';
import { Select, MenuItem } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import DashboardCard from '../../../components/shared/DashboardCard';
import Chart from 'react-apexcharts';

const DTSTables = ({ tableData }) => {
  // select
  const [month, setMonth] = useState('1');

  const handleChange = (event) => {
    setMonth(event.target.value);
  };

  // chart color
  const theme = useTheme();
  const primary = theme.palette.primary.main;
  const secondary = theme.palette.secondary.main;
  const tertiary = theme.palette.error.main;

  // chart
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
      // toolbar:{
      //   offsetX: '100%',
      // }
    },
    colors: [primary, secondary, tertiary],
    dataLabels: {
      enabled: false,
    },
    markers: {
      size: 1,
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
      categories: tableData.map((i) => i['date']),
      type: 'datetime',
      title: {
        text: 'Day',
      },
    },
    yaxis: {
      title: {
        text: 'USD',
      },
      min: Math.min(
        ...tableData.map((i) => i['deposits']),
        ...tableData.map((i) => i['withdrawals']),
        ...tableData.map((i) => i['total']),
      ),
      max: Math.max(
        ...tableData.map((i) => i['deposits']),
        ...tableData.map((i) => i['withdrawals']),
        ...tableData.map((i) => i['total']),
      ),
    },
    legend: {
      position: 'bottom',
    },
  };

  const seriescolumnchart = [
    {
      name: 'Total Deposits',
      data: tableData.map((i) => i['deposits']),
    },
    {
      name: 'Total Withdrawals',
      data: tableData.map((i) => i['withdrawals']),
    },
    {
      name: 'Total Sum',
      data: tableData.map((i) => i['total']),
    },
  ];

  return (
    <DashboardCard title="Deposits and Withdrawals of Operating Cash">
      <Chart options={optionscolumnchart} series={seriescolumnchart} type="line" height="270px" />
    </DashboardCard>
  );
};

export default DTSTables;
